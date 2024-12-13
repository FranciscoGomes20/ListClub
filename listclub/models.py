from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(class)s_created_by", on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(User, related_name="%(class)s_modified_by", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class Categorias(AuditModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Listas(AuditModel):
    usuarios_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Status(AuditModel):
    nome = models.CharField(max_length=100)
    categorias_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)

class Diretor(AuditModel):
    nome = models.CharField(max_length=100)

class Itens(AuditModel):
    listas_id = models.ForeignKey(Listas, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    diretor_id = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.IntegerField()

class Generos(AuditModel):
    nome = models.CharField(max_length=100)

class ItensGenero(AuditModel):
    itens_id = models.ForeignKey(Itens, on_delete=models.CASCADE)
    genero_id = models.ForeignKey(Generos, on_delete=models.CASCADE)
