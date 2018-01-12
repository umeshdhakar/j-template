from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Offer(models.Model):
    title = models.CharField(max_length=20)
    expiry_date = models.DateField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=12)
    date = models.DateTimeField()
    remark = models.CharField(max_length=50, null=True)

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    feedback = models.CharField(max_length=40)
    email = models.CharField(max_length=40, null=True)
    rating = models.IntegerField(null=True)
