from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    bdate = models.DateField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + str(self.age)
