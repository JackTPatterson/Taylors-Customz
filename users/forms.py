from django.forms.fields import BooleanField
from .models import Product, AboutMe, Reviews
from django import forms

SHOE_SIZE = [
	('Select Size', 'Select Size'),
	('5', '5'),
	('5.5', '5.5'),
	('6', '6'),
	('6.5', '6.5'),
	('7', '7'),
	('7.5', '7.5'),
	('8', '8'),
	('8.5', '8.5'),
	('9', '9'),
	('9.5', '9.5'),
	('10', '10'),
	('10.5', '10.5'),
	('11', '11'),
	('11.5', '11.5'),
	('12', '12'),
	('12.5', '12.5'),
	('13', '13'),
	
]

GENDER = [
	('Select Sizing', 'Select Sizing'),
	('Male', 'Male'),
	('Female', 'Female'),
	('Child', 'Child'),
	
]

HASSHOES = [
	('Select Choice', 'Select Choice'),
	('I own these shoes', 'I own these shoes'),
	('I need these shoes', 'I need these shoes'),
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

	address = forms.CharField(label='address', widget=forms.TextInput(
		attrs={

			
			'placeholder': 'Address',
			'class': 'form-control',
		}
	))

	city = forms.CharField(label='city', widget=forms.TextInput(
		attrs={

			
			'placeholder': 'City',
			'id': 'req-form-address',
			'class': 'form-control',
		}
	))



	state = forms.CharField(label='state', widget=forms.TextInput(
		attrs={

			
			'placeholder': 'State',
			'id': 'req-form-address',
			'class': 'form-control',
		}
	))

	postal = forms.CharField(label='ZIP', widget=forms.TextInput(
		attrs={

			
			'placeholder': 'ZIP Code',
			'id': 'req-form-address',
			'class': 'form-control',
		}
	))

	description = forms.CharField(label='Design Description', widget=forms.Textarea(
		attrs={

			'class': 'form-control',
			'placeholder': 'Description',
			'id': 'req-form-desc'
		}
	))

	photo = forms.ImageField(required=False, widget=forms.FileInput(
		 attrs={

			 'type': "file",
			 'class': "custom-file-input",
			 'id': "inputGroupFile01",
			 'required': 'false'

		 }
	 ))

	hasShoe = forms.CharField(widget=forms.Select(choices=HASSHOES))

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
			'placeholder': 'Type of shoe',
			'id': 'req-form-shoe-name',
		}
	))

	class Meta:
		model = Product
		exclude = ['date_submitted', 'completed', 'orderNumber', 'orderId', 'completed', 'started', 'price', 'archived']

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


class CompletedForm(forms.ModelForm):
	
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



class AboutMeForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(
		attrs={

			'class': 'form-control',
			'placeholder': 'About Me Message',
			'id': 'about-msg'
		}
	))

	class Meta:
		model = AboutMe
		exclude = ('active',)

class ReviewForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(
		attrs={

			'class': 'form-control',
			'placeholder': 'About Me Message',
			'id': 'about-msg'
		}
	))

	rating = forms.IntegerField(widget=forms.TextInput(
		attrs={

			'class': 'form-control',
			'placeholder': 'About Me Message',
			'id': 'about-msg'
		}
	))

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

	class Meta:
		model = Reviews
		exclude = ('rating',)

class ReviewEditForm(forms.ModelForm):
	active = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'inp-cbx',
            'style': 'display: none;',
            'id': 'cbx'

        }
    ))

	class Meta:
		model = Reviews
		fields = ('active',)