from django import forms
from django.contrib.auth.models import User
from .models import TonalidadeConfig

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirme a senha')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('password2'):
            raise forms.ValidationError('As senhas não conferem.')
        return cleaned

class LoginForm(forms.Form):
    username = forms.CharField(label='Email ou usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

class TonalidadeForm(forms.ModelForm):
    class Meta:
        model = TonalidadeConfig
        fields = ['tonalidade_1', 'tonalidade_2', 'tonalidade_3']
        widgets = {
            'tonalidade_1': forms.NumberInput(attrs={'type': 'range', 'min': -180, 'max': 180, 'step': 1}),
            'tonalidade_2': forms.NumberInput(attrs={'type': 'range', 'min': 0.5, 'max': 2, 'step': 0.05}),
            'tonalidade_3': forms.NumberInput(attrs={'type': 'range', 'min': 0.5, 'max': 2, 'step': 0.05}),
        }
