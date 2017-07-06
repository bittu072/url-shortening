from django import forms

class URLSubmit(forms.Form):
    url = forms.CharField(label='Submit URL')

    def clean(self):
        cleaned_data = super(URLSubmit, self).clean()
        url = cleaned_data['url']
        print (url)
