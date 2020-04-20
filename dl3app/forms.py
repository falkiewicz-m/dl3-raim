from django import forms

class DL3Form(forms.Form):
	postcode = forms.CharField(label='Kod pocztowy')