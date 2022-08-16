from django.db import DatabaseError, models

# makemigrations - create changes in Database
# migrate-do the pending changes to complete db


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()



    def __str__(self):
        return self.name
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Snacks(models.Model):
    name = models.CharField(max_length=20)
    Price = models.IntegerField(default=0)
    description = models.TextField(default='', max_length=250)
    image = models.ImageField(upload_to="web1/dbimages/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name



class feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    feedb = models.TextField()

    
    def __str__(self):
        return self.name






