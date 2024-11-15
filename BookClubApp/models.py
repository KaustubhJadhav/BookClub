from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    summary = models.TextField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='books')
    added_at = models.DateTimeField(auto_now_add=True)
