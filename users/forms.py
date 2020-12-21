from .models import Product
from django import forms

SHOE_SIZE = [
    ('Select Size', 'Select Size'),
    ('7', '7'),
    ('8', '8'),
]

GENDER = [
    ('Select Gender', 'Select Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
]


class ProductCreationForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={

            'class': 'form-control',
            'placeholder': 'First Name',
            'id': 'req-form-fName'
        }
    ))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={

            'class': 'form-control',
            'placeholder': 'Last Name',
            'id': 'req-form-lName'
        }
    ))

    description = forms.CharField(label='Design Description', widget=forms.Textarea(
        attrs={

            'class': 'form-control',
            'placeholder': 'Description',
            'id': 'req-form-desc'
        }
    ))

    photo = forms.ImageField(widget=forms.FileInput(
         attrs={

             'type': "file",
             'class': "custom-file-input",
             'id': "inputGroupFile01",

         }
     ))

    hasShoe = forms.BooleanField(widget=forms.CheckboxInput(
         attrs={
             'class': 'inp-cbx',
             'style': 'display: none;',
             'id': 'cbx'
         }
     ))

    email = forms.EmailField(widget=forms.EmailInput(
         attrs={
             'class': 'form-control',
             'placeholder': 'Email Address',
             'id': 'req-form-email'
         }
    ))

    shoe_size = forms.CharField(widget=forms.Select(choices=SHOE_SIZE))

    gender = forms.CharField(widget=forms.Select(choices=GENDER))

    shoe_name = forms.CharField(widget=forms.TextInput(
         attrs={

            'class': 'form-control',
            'placeholder': 'Shoe Name',
            'id': 'req-form-shoe-name'
        }
    ))

    class Meta:
        model = Product
        exclude = ['date_submitted', 'completed', 'orderNumber', 'orderId', 'completed', 'started', 'price']

class AcceptForm(forms.ModelForm):

    price = forms.CharField(widget=forms.TextInput(
        attrs={

            'class': 'form-control',
            'placeholder': 'Price',
            'id': 'prc-form'
        }
    ))

    message = forms.CharField(widget=forms.Textarea(
        attrs={

            'class': 'form-control',
            'placeholder': 'Custom Message',
            'id': 'custom-msg'
        }
    ))
    class Meta:
        model = Product
        fields = ('price', 'message')

class DenyForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(
        attrs={

            'class': 'form-control',
            'placeholder': 'Custom Message',
            'id': 'custom-msg'
        }
    ))
    class Meta:
        model = Product
        fields = ('message',)

class EmailForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(
        attrs={

            'class': 'form-control',
            'placeholder': 'Custom Message',
            'id': 'custom-msg'
        }
    ))
    class Meta:
        model = Product
        fields = ('message',)