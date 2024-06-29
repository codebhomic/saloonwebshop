# forms.py
from django import forms
from .models import Appointment, Content 

class TitleCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        option['label'] = value.instance.title  # Use the title of the Content instance
        return option

class AppointmentForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Content.objects.filter(category__name='Services'),
        widget=TitleCheckboxSelectMultiple(attrs={'class': 'mx-2'}),
        label="Services",
    )
    appointment_date = forms.DateField(
        widget=forms.SelectDateWidget(attrs={'class': 'form-control w-full mt-1'})
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control w-full mt-1'})
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-textarea mt-1 block w-full', 'rows': 3}),
        required=False
    )

    class Meta:
        model = Appointment
        fields = ['services', 'appointment_date', 'start_time', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'services':  # services already have custom widget classes
                field.widget.attrs.update({'class': 'form-control w-full mt-1'})
