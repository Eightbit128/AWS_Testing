# import the standard Django Forms
# from built-in library
from django import forms


# creating a form
class InputForm(forms.Form):
    Text_to_reverse = forms.CharField(max_length=200, required=False)
    Text_to_format = forms.CharField(max_length=200, required=False)
