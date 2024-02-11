from django.db import models
from django import forms

# Create your models here.

class Fruta(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class FrutaForm(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = ['nome', 'cor', 'preco']