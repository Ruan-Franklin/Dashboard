from django.db import models
from django import forms 
class Diretoria(models.Model):    
  #  Id = models.IntegerField()
    nome = models.CharField(max_length=10, default='')
    turmas = models.CharField(max_length=150,null=True)
    salas = models.CharField(max_length=100,null=True)    
    professores = models.CharField(max_length=100,null=True)
    cargas = models.CharField(max_length=30,null=True)        
    DOB = models.DateField(null=True, blank=True)     
     
      
 
    def __str__(self):
        return self.nome
                 
    objects = models.Manager()
'''
    class Diretoria(models.Model):
      nome=models.CharField(max_length=255),
      turmas=models.CharField(max_length=2),
      salas=models.CharField(max_length=2),
      professores= models.IntegerField(blank=True, null=True)
      carga=models.IntegerField(blank=True, null= True)

'''