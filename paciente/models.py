from django.db import models
import uuid
# Create your models here.
class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(unique=True, null=True, blank=True, max_length=14)
    data_nascimento = models.DateField()
    telefone = models.CharField(null=True, max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.data_nascimento}, {self.telefone}, {self.criado_em}"
        