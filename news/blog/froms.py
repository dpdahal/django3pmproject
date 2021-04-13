from django import forms
from blog.models import Contact


class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if len(full_name) < 5:
            raise forms.ValidationError("Name at least 3 character")

        return full_name
