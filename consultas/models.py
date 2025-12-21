from django.db import models
import uuid
from profissionais.models import Profissional
from paciente.models import Paciente
# Create your models here.
class Consulta(models.Model):

    status_choice = [
        ('AGENDADA', 'Agendada'),
        ('CANCELADA', 'Cancelada'),
        ('REALIZADA', 'Realizada')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profissional = models.ForeignKey(
            Profissional, 
            on_delete=models.PROTECT, 
            related_name='consultas'
        )
    paciente = models.ForeignKey(
        Paciente,
        on_delete= models.PROTECT,
        related_name='consultas'
    )
    data = models.DateTimeField()
    status = models.CharField(max_length=10, null=True, choices=status_choice, default='Agendada')
    criado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['criado_em']
    
    def __str__(self):
        return f'{self.paciente.nome} com {self.profissional.nome} em {self.data}'
