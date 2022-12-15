from .models import Stay, Review
from django.forms import ModelForm
from django.forms import ValidationError


class StayForm(ModelForm):
    class Meta:
        model = Stay
        fields = ['owner', 'provider', 'start_date', 'end_date', 'pets']

    def clean(self):
        cleaned_data = super().clean()
        owner = cleaned_data.get("owner")
        provider = cleaned_data.get("provider")
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if owner == provider.person:
            self.add_error('provider', 'You cannot perform a stay for yourself')
        if end_date < start_date:
            self.add_error('end_date', 'End date should be greater than start date.')
        return cleaned_data


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating']

    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get("rating")

        if int(rating) > 5:
            self.add_error('rating', 'You can choose between 1 and 5')
        return cleaned_data
