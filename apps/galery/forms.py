from django import forms
from apps.galery.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'nome': 'Name',
            'legenda': 'Caption',
            'categoria': 'Category',
            'descricao': 'Description',
            'foto': 'Photo',
            'data_fotografia': 'Date',
            'user': 'User',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                    }
                ),
            'user': forms.Select(attrs={'class': 'form-control'})
        }