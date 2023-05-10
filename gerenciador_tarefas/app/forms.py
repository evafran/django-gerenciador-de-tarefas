#from tkinter.tix import Form
from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
  class Meta:
      model = Tarefa
      exclude = ('usuario',)
      fields = '__all__'
   