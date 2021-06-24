from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Last Name'}))
    phone_number = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'E-mail'}))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords Do Not Match')
