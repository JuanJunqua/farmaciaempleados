from django import forms
from .models import encargado, mostrador, subencargado

class EncargadoForm(forms.ModelForm):
    class Meta:
        model = encargado
        fields = '__all__'

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        try:
            int(telefono)
        except ValueError:
            raise forms.ValidationError('Telefono tiene que ser un numero')
        return telefono

class SubencargadoForm(forms.ModelForm):
    class Meta:
        model = subencargado
        fields = '__all__'

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        try:
            int(telefono)
        except ValueError:
            raise forms.ValidationError('Telefono tiene que ser un numero')
        return telefono

class MostradorForm(forms.ModelForm):
    class Meta:
        model = mostrador
        fields = '__all__'

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        try:
            int(telefono)
        except ValueError:
            raise forms.ValidationError('Telefono tiene que ser un numero')
        return telefono