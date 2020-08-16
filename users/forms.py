from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.mail import send_mail

from .models import Profile, User
from django_countries.fields import CountryField
import logging

logger = logging.getLogger(__name__)


class UserRegisterForm(UserCreationForm):
    # user_type = forms.ChoiceField(widget=forms.HiddenInput(), choices=USER_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']
        field_classes = {"email": UsernameField}

    def send_mail(self):
        logger.info(
            "Sending Signup email for username=%s",
            self.cleaned_data["username"]
        )
        message = "Welcome {}".format(self.cleaned_data["username"])
        send_mail(
            "Welcome to Me2U|Africa",
            message,
            "me2uafrica.herokuapp.com",
            [self.cleaned_data["username"]],
            fail_silently=True,
        )


# class AutomobileRegisterForm(UserCreationForm):
#     phone_number = forms.CharField(max_length=20)
#     refferal_name = forms.CharField(max_length=10)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email,' 'password1', 'password2']

#
# class SellerRegisterForm(UserCreationForm):
#     shop_tax_country = CountryField(multiple=False)
#     phone_number = forms.CharField(max_length=20)
#     refferal_name = forms.CharField(max_length=10)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email,' 'password1', 'password2']


class AddressForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = Profile
    #     exclude = ['user', 'image', 'email', 'phone']


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image']
