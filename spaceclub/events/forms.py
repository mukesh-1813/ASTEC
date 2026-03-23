from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['name', 'email', 'phone', 'college']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:border-blue-500', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:border-blue-500', 'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:border-blue-500', 'placeholder': 'Your Phone Number'}),
        }

class PaymentVerificationForm(forms.ModelForm):
    transaction_id = forms.CharField(
        max_length=100, 
        required=True,
        min_length=12,
        help_text="Enter the 12-digit transaction ID from your UPI app.",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-space-800 border-2 border-purple-500/30 rounded-xl text-white focus:outline-none focus:border-purple-500 transition-colors', 
            'placeholder': 'e.g. 312345678901'
        })
    )

    class Meta:
        model = EventRegistration
        fields = ['transaction_id']

    def clean_transaction_id(self):
        tid = self.cleaned_data.get('transaction_id')
        if tid:
            tid = tid.strip()
            if not tid.isalnum():
                raise forms.ValidationError("Transaction ID should only contain letters and numbers.")
        return tid
