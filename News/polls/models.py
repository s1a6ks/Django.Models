from django.db import models


class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title