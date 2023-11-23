from django import forms
from .models import encargado, mostrador, subencargado
from django.contrib.auth.models import User
from django import forms
from .models import Message


class BaseEmpleadoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['empleo'].widget.attrs['readonly'] = True

class EncargadoForm(BaseEmpleadoForm):
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

class SubencargadoForm(BaseEmpleadoForm):
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

class MostradorForm(BaseEmpleadoForm):
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

