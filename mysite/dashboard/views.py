from .models import Diretoria
#from .services import ImportToDatabase
import datetime as dt
import pandas as pd
import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

 
def Import_csv(request):
    
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
           # meuarquivo=import_data()        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                '''
                nome = models.CharField(max_length=10, default='')
    turmas = models.CharField(max_length=150,null=True)
    salas = models.CharField(max_length=100,null=True)    
    professores = models.CharField(max_length=100,null=True)
    cargas = models.CharField(max_length=30,null=True)        
    DOB = models.DateField(null=True, blank=True)     
                '''
                 
                fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = Diretoria.objects.create(nome=dbframe.nome, turmas=dbframe.turmas,
                                                salas=dbframe.salas,  professores=dbframe.professores, cargas=dbframe.cargas, 
                                                DOB=fromdate_time_obj,
                                                )
                print(type(obj))
                obj.save()
 
            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'importexcel.html',{})

