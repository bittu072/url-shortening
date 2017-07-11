from django import forms

from .validators import validate_url, validate_dot_com


class URLSubmit(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])

    # def clean(self):
    #     cleaned_data = super(URLSubmit, self).clean()
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #     return url
        # print (url)

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     print (url)
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
        # return url
