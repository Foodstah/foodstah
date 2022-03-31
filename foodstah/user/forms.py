from django import forms

from .models import Profile


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            "password": forms.PasswordInput(),
        }
        fields = ["email", "username", "password", "first_name"]

    def save(self, commit=True):
        user = super(NewProfileForm, self).save()
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user