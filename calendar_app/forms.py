from django import forms
from .models import CalendarEntry

class DateInput(forms.DateInput):
    input_type = 'date'

class CalendarEntryForm(forms.ModelForm):
    class Meta:
        model = CalendarEntry
        fields = ['title', 'description', 'date', 'entry_type']
        widgets = {
            'date': DateInput(),
            'description': forms.Textarea(attrs={'rows': 4}),
        }