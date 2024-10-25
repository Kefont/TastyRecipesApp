from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef', 'bio']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name[0].isupper():
            raise forms.ValidationError('First Name must start with a capital letter!')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name[0].isupper():
            raise forms.ValidationError('Last Name must start with a capital letter!')
        return last_name
