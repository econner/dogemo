from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone = forms.CharField(max_length=20, label='Phone Number')

    class Meta:
        model = get_user_model()

    def save(self, user):
        #user.save()
        pass