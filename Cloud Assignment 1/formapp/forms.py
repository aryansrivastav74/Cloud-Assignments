import re
from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['email', 'name', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if UserData.objects.filter(email=email).exists():
            raise forms.ValidationError("Already Registered")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        pattern = r'^[A-Z][A-Za-z0-9!@#$%^&*()]{7,}$'

        if not re.match(pattern, password):
            raise forms.ValidationError(
                "Password must start with a capital letter, "
                "contain at least 8 characters, include one number "
                "and one special character (!@#$%^&*())."
            )

        if not re.search(r"[0-9]", password):
            raise forms.ValidationError(
                "Password must include at least one number."
            )

        if not re.search(r"[!@#$%^&*()]", password):
            raise forms.ValidationError(
                "Password must include at least one special character (!@#$%^&*())."
            )

        return password
