from django import forms
class  contactform(forms.Form):
    name = forms.CharField(required='true', max_length=20)
    email = forms.EmailField(max_length=50)
    city = forms.ChoiceField(choices=[('None', '__Select__'), ('Hyderabad', 'Hyd'), ('Chennai','che')])
    mobile = forms.CharField(max_length=10)