from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("Title", max_length=50)
    anons = models.CharField("Anons", max_length=250)
    full_text = models.TextField("Article")
    date = models.DateTimeField("Publication date")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'