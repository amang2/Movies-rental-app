
from users.models import UserProfile
from movies.serializers import MovieSerializer
from movies.models import Movie
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Count, Sum
from django.utils.timezone import now, timedelta
from rest_framework import generics
from rest_framework.response import Response
from .models import Genre, Movie, Rental
from .serializers import CustomerSerializer, GenreSerializer, MovieSerializer, RentalSerializer
from rest_framework import status


class MovieListCreateView(ListCreateAPIView):
    """
    This class is created movie and fetch movies list.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def get_queryset(self):
    #     customer_id = self.kwargs['customer_id']
    #     return Movie.objects.filter(rental__customer_id=customer_id).annotate(rental_count=Count('rental')).filter(rental_count__gt=5)

# class GenreListCreateView





class CustomerRentedMoviesView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    
    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Movie.objects.filter(rental__customer_id=customer_id).annotate(rental_count=Count('rental')).filter(rental_count__gt=5)
    

class PopularGenresView(generics.ListAPIView):
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.annotate(movie_count=Count('movie')).filter(movie_count__gte=10)

class MoviesRentedLastMonthView(generics.ListAPIView):
    serializer_class = RentalSerializer

    def get_queryset(self):
        last_month = now() - timedelta(days=30)
        return Rental.objects.filter(rental_date__gte=last_month)

class TotalRevenueLastQuarterView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        last_quarter = now() - timedelta(days=90)
        total_revenue = Rental.objects.filter(rental_date__gte=last_quarter).aggregate(total_revenue=Sum('movie__price'))
        return Response(total_revenue)

class CustomersMultipleGenresView(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return UserProfile.objects.annotate(genre_count=Count('rentals__movie__genres', distinct=True)).filter(genre_count__gt=3)

class RentalCreateView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def create(self, request, *args, **kwargs):
        customer_id = request.data.get('customer')
        movie_id = request.data.get('movie')

        try:
            customer = UserProfile.objects.get(id=customer_id)
            movie = Movie.objects.get(id=movie_id)
        except (UserProfile.DoesNotExist, Movie.DoesNotExist):
            return Response({'error': 'Customer or Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        # # Check if the movie is available for rent
        # if movie.available_copies < 1:
        #     return Response({'error': 'Movie is not available for rent'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the rental
        rental = Rental.objects.create(customer=customer, movie=movie)
        movie.save()

        return Response(RentalSerializer(rental).data, status=status.HTTP_201_CREATED)