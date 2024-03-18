from django.db import models

# Create your models here.
class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    date_released = models.DateField()
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Movie'