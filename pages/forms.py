from pages.models import Contact
from django import forms

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@gmail.com' in email:
            raise forms.ValidationError('you can just us gmail account')
        return email
