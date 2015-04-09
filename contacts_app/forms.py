from contacts_app.models import Contact
from django import forms

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','number']
        


