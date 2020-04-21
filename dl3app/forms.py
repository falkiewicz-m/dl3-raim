from django import forms

class DL3Form(forms.Form):
	kod = forms.CharField(label='Kod pocztowy')