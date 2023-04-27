from django.db import models
#Create your models here.
#ListView
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    pages=models.IntegerField()
    price=models.FloatField()



#DetailView
from django.db import models
class Company(models.Model):
    name=models.CharField(max_length=128)
    location=models.CharField(max_length=64)
    ceo=models.CharField(max_length=64)
    def __str__(self):		##add-this extra-code
        return self.name;

#extra-table
class Employee(models.Model):   #child-table
    eno=models.IntegerField()
    name=models.CharField(max_length=128)
    salary=models.FloatField()
    company=models.ForeignKey(Company,related_name='employees',on_delete=models.CASCADE)
