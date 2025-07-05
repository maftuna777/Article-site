from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    info = models.TextField(blank=True)
    photo = models.ImageField(upload_to="images/", blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return "https://static.vecteezy.com/system/resources/previews/022/059/000/non_2x/no-image-available-icon-vector.jpg"

class Comment(models.Model):
    text=models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text