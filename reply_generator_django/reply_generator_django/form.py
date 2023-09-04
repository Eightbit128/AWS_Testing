from django import forms



class InputForm(forms.Form):
    Text_to_reverse = forms.CharField(max_length=200, required=False)
    Text_to_format = forms.CharField(max_length=200, required=False)
