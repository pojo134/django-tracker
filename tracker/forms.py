from django import forms
from .models import Medicine, FREQUENCY_CHOICES

class MedicineForm(forms.ModelForm):
    frequency = forms.ChoiceField(
        choices=FREQUENCY_CHOICES,
        initial='daily',
        widget=forms.RadioSelect(attrs={'class': 'flex gap-4'})
    )
    dose_count = forms.IntegerField(
        min_value=1,
        max_value=10,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'input input-bordered'})
    )

    class Meta:
        model = Medicine
        fields = ['name', 'dosage', 'frequency', 'dose_count']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input input-bordered'})
        self.fields['dosage'].widget.attrs.update({'class': 'input input-bordered'})
