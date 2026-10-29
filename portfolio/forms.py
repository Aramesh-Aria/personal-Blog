from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class RefreshableCaptchaInput(CaptchaTextInput):
    template_name = 'portfolio/captcha_widget.html'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(max_length=120, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    subject = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 6}))
    captcha = CaptchaField(widget=RefreshableCaptchaInput(attrs={'class': 'form-control', 'placeholder': 'Enter the code above', 'autocomplete': 'off'}))
