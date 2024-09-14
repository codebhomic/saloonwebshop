from django import forms
from pages.models import ContactModel
class ContactForm(forms.ModelForm):
    classess="w-full bg-white rounded border border-gray-300 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
    name = forms.CharField(max_length=100,required=True,label="Name: ",widget=forms.TextInput({"class":classess,"placeholder":"enter your name"}))
    phone = forms.IntegerField(required=True,widget=forms.NumberInput({"class":classess,"placeholder":"enter your phone number"}))
    email = forms.EmailField(required=True,widget=forms.EmailInput({"class":classess,"placeholder":"enter your email address"}))
    COLOR_CHOICES = [
        ('hairstyle', 'Hairstyle'),
        ('wax', 'Wax'),
        ('pedicure', 'Pedicure'),
        ('manicure', 'Manicure'),
        ('facials', 'Facials'),
        ('others', 'Others'),
    ]
    services = forms.ChoiceField(choices=COLOR_CHOICES,widget=forms.Select({"class":classess,"label":"Regarding what service"}))
    # services = forms.ChoiceField({"class":classess,"label":"Regarding what service"},choices=("Hairstyle","","facial","others"))
    message = forms.CharField(widget=forms.Textarea({"class":classess,"placeholder":"enter your message"}))

    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone', 'services', 'message']