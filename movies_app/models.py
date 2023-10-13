from django.db import models

# movies_app/models.py

from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    liked = models.BooleanField()

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {'Liked' if self.liked else 'Disliked'}"

class Match(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user1 = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie', 'user1', 'user2')

    def __str__(self):
        return f"Match: {self.movie.title} - {self.user1.username} and {self.user2.username}"
