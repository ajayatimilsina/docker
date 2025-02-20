from django import forms

class StudentRegistrationForm(forms.Form):
    photo = forms.ImageField(label='Photo')
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=15)
    address = forms.CharField(label='Address', widget=forms.Textarea)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
