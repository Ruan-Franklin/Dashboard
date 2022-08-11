from .models import Diretoria
class ImportToDatabase(object):

    @staticmethod
    def import_data():
        with open('DadosAtividadePratica.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                obj, created = Diretoria.objects.get_or_create(
                    nome=row[0],
                    turmas=row[1],
                    salas=row[2],
                    professores=row[3],
                    carga=row[4],
                )

'''
turmas=models.CharField(max_length=2),
      salas=models.CharField(max_length=2),
      professores= models.IntegerField(blank=True, null=True)
      carga=models.IntegerField(blank=True, null= True)
'''