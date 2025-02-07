from django.db import models

# Create your models here.

class ContaBancaria(models.Model):
    nome = models.CharField(max_length=512, null=False)
    cpf = models.CharField(max_length=9, unique=True)
    senha = models.CharField(max_length=9, null=False)
    saldo = models.FloatField( null=False)
    telefone = models.CharField(max_length=11, null=False)

    def __str__(self):
        return f'Correntista#{self.id} com saldo R$ {self.saldo}'


class ChavePix(models.Model):
    descricao = models.CharField(max_length=512, null=False, unique=True)
    conta = models.ForeignKey(ContaBancaria, on_delete=models.CASCADE)

    def __str__(self):
        return f'A chave {self.descricao} pertence a(o) {self.conta.nome}'