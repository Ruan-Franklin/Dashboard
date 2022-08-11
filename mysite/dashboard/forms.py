from django import forms
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
 
from .models import Diretoria
 
class DiretoriaRegistration(forms.ModelForm):
    class Meta:
        model = Diretoria
        fields =[ 'nome','turmas','salas','professores' ,'cargas',
                  'DOB','gender','qualification'
        ] 
'''
        nome = models.CharField(max_length=10, default='')
    turmas = models.CharField(max_length=150,null=True)
    salas = models.CharField(max_length=100,null=True)    
    professores = models.CharField(max_length=100,null=True)
    cargas = models.CharField(max_length=30,null=True)        
    DOB = models.DateField(null=True, blank=True)     '''