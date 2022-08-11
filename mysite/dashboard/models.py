from django.db import models
from django import forms 
class tbl_Employee(models.Model):    
  #  Id = models.IntegerField()
    Empcode = models.CharField(max_length=10, default='')
    firstName = models.CharField(max_length=150,null=True)
    middleName = models.CharField(max_length=100,null=True)    
    lastName = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=30,null=True)
    phoneNo = models.CharField(max_length=12, default='',null=True)
    address = models.CharField(max_length=500, default='',null=True) 
    exprience = models.CharField(max_length=50, default='',null=True)        
    DOB = models.DateField(null=True, blank=True)   
    gender = models.CharField(max_length=10, default='',null=True)
    qualification = models.CharField(max_length=50,default='',null=True)   
     
      
 
    def __str__(self):
        return self.firstName
                 
    objects = models.Manager()
'''
    class Diretoria(models.Model):
      nome=models.CharField(max_length=255),
      turmas=models.CharField(max_length=2),
      salas=models.CharField(max_length=2),
      professores= models.IntegerField(blank=True, null=True)
      carga=models.IntegerField(blank=True, null= True)

'''