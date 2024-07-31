from django.urls import path
from .views import CustomerRentedMoviesView, CustomersMultipleGenresView, MovieListCreateView, MovieRetrieveUpdateDestroyView, MoviesRentedLastMonthView, PopularGenresView, RentalCreateView, TotalRevenueLastQuarterView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-retrieve-update-destroy'),
    path('customer/<int:customer_id>/rented-movies/', CustomerRentedMoviesView.as_view(), name='customer-rented-movies'),
    path('popular-genres/', PopularGenresView.as_view(), name='popular-genres'),
    path('movies-rented-last-month/', MoviesRentedLastMonthView.as_view(), name='movies-rented-last-month'),
    path('total-revenue-last-quarter/', TotalRevenueLastQuarterView.as_view(), name='total-revenue-last-quarter'),
    path('customers-multiple-genres/', CustomersMultipleGenresView.as_view(), name='customers-multiple-genres'),
    path('rentals/', RentalCreateView.as_view(), name='rental-create'),

]

