from django import forms

class URLSubmit(forms.Form):
    url = forms.CharField(label='Submit URL')
