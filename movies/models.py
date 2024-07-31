from users.models import UserProfile
from django.db import models
from db.base_model import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre,related_name="moview_genre")

    def __str__(self):
        return self.title


class Rental(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_on_rental")
    rental_date = models.DateField()
    return_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.movie.title} rented by {self.customer.user.username}'





