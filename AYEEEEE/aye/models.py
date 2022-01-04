from django.db import models
from django.db import connections
# Create your models here.

class EmployeeDetails(models.Model):

    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    apartament=models.CharField(max_length=100)
    kakayato_hren = models.ForeignKey('categories', on_delete=models.PROTECT, null=True)
    class Meta:
        db_table='aye'


    def get_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
