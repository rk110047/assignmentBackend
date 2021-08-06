from django.db import models

# Create your models here.


class UserDetails(models.Model):
    name            =       models.CharField(max_length=120)
    date_of_birth   =       models.DateField()
    email           =       models.EmailField()
    phone_number    =       models.CharField(max_length=10)


    def __str__(self):
        return self.name
