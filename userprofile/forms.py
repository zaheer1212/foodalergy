from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from products.models import Allergy


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254,)
    allergies = forms.ModelMultipleChoiceField(queryset=Allergy.objects.all(), widget=forms.CheckboxSelectMultiple(), help_text='Required. Please select the allergies that impact your family.')
    i_agree = forms.BooleanField(help_text='to these <a href="/" target="_blank">terms and conditions</a>')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'allergies', 'i_agree' )

class UpDateForm(UserChangeForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.')
    allergies = forms.ModelMultipleChoiceField(queryset=Allergy.objects.all(), widget=forms.CheckboxSelectMultiple(), help_text='Required. Please select the allergies that impact your family.')

    class Meta:
        model = User
        fields = ('username', 'email', 'allergies')

    def clean_password(self):
            # Regardless of what the user provides, return the initial value.
            # This is done here, rather than on the field, because the
            # field does not have access to the initial value
            return ""