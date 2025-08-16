from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@objor.com'):
            raise ValidationError("Email must end with '@objor.com'.")
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email is already taken.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken.")
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and CustomUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("Phone number is already taken.")
        return phone_number

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user