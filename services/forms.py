from django import forms
from .models import ContactClient


class ContactClientForm(forms.ModelForm):
    class Meta:
        model = ContactClient
        fields = [
            'name',
            'phone'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'messages', 'id': "Имя",
                                           'placeholder': "Введите ваше имя"
                                           }),
            'phone': forms.TextInput(attrs={'class': "messages", 'id': "Телефон",
                                            'placeholder': "Введите ваш номер телефона"}),
        }


