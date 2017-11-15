from django import forms
from django.core.exceptions import ValidationError
from userdb.models import Users

'''
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        name = all_clean_data['name']
        email = all_clean_data['email']

        if 'bb' in email:
            raise ValidationError('PROHIBITED EMAIL!') 
'''
class FormModel(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'
