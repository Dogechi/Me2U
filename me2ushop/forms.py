from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = {

    ('M', "M-Pesa"),
    ('P', "Paypal"),
    ('S', "Stripe"),
    ('D', "Debit Card"),
    ('C', "Cash On Delivery"),

}


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_zip = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))

    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Coupon',
        'class': 'form-control',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Quantity',
        'class': 'form-control',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control col-md-12 mb-4"'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control col-md-12 mb-4"'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control col-md-12 mb-4"'
    }))


class PaymentForm(forms.Form):
    use_default = forms.BooleanField(required=False)
    save = forms.BooleanField(required=False)

