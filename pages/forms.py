from pages.models import Contact
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):

    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name','email','subject','message','captcha']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@gmail.com' in email:
            raise forms.ValidationError('you can just us gmail account')
        return email
