from django.db import models
from django import forms
import random

# Create your models here.

class Cor(models.Model):
    id = models.CharField(primary_key=True, max_length=10, unique=True)
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = ''.join(random.choices('0123456789', k=10))
        super().save(*args, **kwargs)


class CorForm(forms.ModelForm):
    class Meta:
        model = Cor
        fields = ['nome']