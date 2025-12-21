from django.db import models
import uuid
# Create your models here.
class Profissional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=255)
    crm = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nome}; {self.especialidade}; {self.crm}"
