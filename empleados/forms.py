from django import forms
from .models import encargado, mostrador, subencargado
from django.contrib.auth.models import User
from django import forms
from .models import Message
from django.forms.widgets import HiddenInput



class EncargadoForm(forms.ModelForm):
    class Meta:
        model = encargado
        exclude = ['creador', 'empleo']

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
        exclude = ['creador', 'empleo']
        

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
        exclude = ['creador', 'empleo']
        
        

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        try:
            int(telefono)
        except ValueError:
            raise forms.ValidationError('Telefono tiene que ser un numero')
        return telefono
    



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'receiver']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MessageForm, self).__init__(*args, **kwargs)

        if user:
            
            self.fields['receiver'].queryset = User.objects.exclude(username=user.username)
            self.fields['receiver'].widget.attrs['class'] = 'form-control'  

