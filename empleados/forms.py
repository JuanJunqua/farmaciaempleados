from django import forms
from .models import encargado, mostrador, subencargado

class EncargadoForm(forms.ModelForm):
    class Meta:
        model = encargado
        fields = '__all__'

class MostradorForm(forms.ModelForm):
    class Meta:
        model = mostrador
        fields = '__all__'

class SubencargadoForm(forms.ModelForm):
    class Meta:
        model = subencargado
        fields = '__all__'

