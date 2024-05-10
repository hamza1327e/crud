from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from app.models import RecordTable


class Record(forms.ModelForm):
    class Meta:
        model = RecordTable
        fields = ['first_name', 'last_name', 'email', 'phone', 'city']

    first_name = forms.CharField(
        label='First Name',
        error_messages={'required': 'Please Enter Your first Name'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please Enter first Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        error_messages={'required': 'Please Enter Your Last Name'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please Enter Last Name',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        error_messages={'required': 'Please Enter Your Email'},
        widget=forms.TextInput(attrs={
            'placeholder': 'xyz@gmail.com',
            'class': 'form-control'
        })
    )

    phone = forms.CharField(
        label='Phone No',
        error_messages={'required': 'Please Enter Your Phone No'},
        widget=forms.TextInput(attrs={
            'placeholder': '+923075239903',
            'class': 'form-control'
        })
    )

    city = forms.CharField(
        label='Enter your city',
        error_messages={'required': 'Please Enter Your city'},
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter city',
            'class': 'form-control'
        })
    )
