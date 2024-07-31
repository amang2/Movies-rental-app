from users.models import UserProfile
from rest_framework import serializers
from .models import Genre, Movie, Rental



class GenreSerializer(serializers.ModelSerializer):
    public_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Genre
        fields = ['public_id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        slug_field='public_id',
        queryset=Genre.objects.all(),
        source='genre'
    )
    genre_details = GenreSerializer(source='genre', many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['public_id','title', 'description', 'release_date', 'rating', 'genres', 'genre_details']
        read_only_fields = ['public_id']

    def to_internal_value(self, data):
        genres_data = data.get('genres', [])
        validated_genres = []

        for public_id in genres_data:
            try:
                genre = Genre.objects.get(public_id=public_id)
                validated_genres.append(genre)
            except Genre.DoesNotExist:
                raise serializers.ValidationError({
                    'genres': f"Genre with public_id {public_id} does not exist."
                })

        data['genre'] = validated_genres
        return super().to_internal_value(data)


    def create(self, validated_data):
        genres_data = validated_data.pop('genre')
        movie = Movie.objects.create(**validated_data)
        
        movie.genre.set(genres_data)
        return movie

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genre')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        instance.genre.set(genres_data)
        return instance



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'