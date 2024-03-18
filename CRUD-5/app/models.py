from django.db import models

# Create your models here.
class Store(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    quantity = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Store'
        