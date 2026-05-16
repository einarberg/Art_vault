from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class ContactForm(forms.Form):
    street_name = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=20)
    country = CountryField().formfield(widget=CountrySelectWidget())
    national_id = forms.CharField(max_length=20, label="National ID (Kennitala)")


class PaymentForm(forms.Form):
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit card'),
        ('bank_transfer', 'Bank transfer'),
        ('wire_transfer', 'Wire transfer')
    ]
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)

    #credit card fields
    cardholder_name = forms.CharField(required=False, max_length=100)
    card_number = forms.CharField(required=False, max_length=16)
    expiry_date = forms.CharField(required=False, max_length=7, help_text="MM/YYYY")
    cvc = forms.CharField(required=False, max_length=4)

    #bank transfer fields
    iban = forms.CharField(required=False, max_length=34, label="IBAN")

    #wire transfer fields
    sending_bank = forms.CharField(required=False, max_length=100)
    routing_number = forms.CharField(required=False, max_length=20)
    account_number = forms.CharField(required=False, max_length=30)

    def clean(self):
        cleaned_data = super().clean()
        method = cleaned_data.get('payment_method')

        if method == 'credit_card':
            required = ['cardholder_name', 'card_number', 'expiry_date', 'cvc']
        elif method == 'bank_transfer':
            required = ['iban']
        elif method == 'wire_transfer':
            required = ['sending_bank', 'routing_number', 'account_number']
        else:
            required = []

        for field in required:
            if not cleaned_data.get(field):
                self.add_error(field, "This field is required")


        return cleaned_data