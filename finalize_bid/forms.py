from  django import forms

PAYMENT_CHOICES = [
    ('credit', 'Credit Card'),
    ('bank', 'Bank Transfer'),
    ('wire', 'Wire Transfer'),
]

class ContactForm(forms.Form):
    street = forms.CharField(max_length=255,label='Street Address')
    city = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=20)
    national_id = forms.CharField(max_length=20)
    country = forms.ChoiceField(choices=[
        ('Iceland', 'Iceland'),
        ('Norway', 'Norway'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
    ])

class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, weidget=forms.RadioSelect)

    cardholder_name = forms.CharField(max_length=100, required=False)
    card_number = forms.CharField(max_length=16, required=False)
    expiry_date = forms.CharField(max_length=5 ,required=False)
    cvc = forms.CharField(max_length=4, required=False)

    bank_account = forms.CharField(max_length=100, required=False)

    bank_name = forms.CharField(max_length=100, required=False)
    routing_number = forms.CharField(max_length=100, required=False)
    account_number = forms.CharField(max_length=100, required=False)