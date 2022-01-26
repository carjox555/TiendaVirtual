from tkinter.tix import Form
from django import forms
from django.http import request

class FormularioContact(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()