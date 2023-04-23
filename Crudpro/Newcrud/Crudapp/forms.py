from django import forms
from Crudapp.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'