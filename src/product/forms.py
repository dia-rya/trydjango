from django import forms 
from .models import product

class productform(forms.ModelForm):
	class Meta:
		model = product 
		fields = [
			'title',
			'description',
			'price'
		]

class rawproductform(forms.Form):
	title		= forms.CharField()
	description = forms.CharField()
	price 		= forms.DecimalField()
