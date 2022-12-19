from .models import Stay, Review
from django.forms import ModelForm
from datetime import date


class StayForm(ModelForm):
    class Meta:
        model = Stay
        fields = ['owner', 'provider', 'start_date', 'end_date', 'pets']

    def clean_start_date(self):
        now = date.today()
        data = self.cleaned_data['start_date']
        if data and data > now:
            self.add_error('start_date', 'Pick a valid date')
        return data

    def clean_end_date(self):
        now = date.today()
        data = self.cleaned_data['end_date']
        if data and data > now:
            self.add_error('end_date', 'Pick a valid date')
        return data

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
        fields = ['review', 'rating']

    def clean_review(self):
        cleaned_data = super().clean()
        review = cleaned_data.get('review')
        if review and len(review) < 1:
            self.add_error('review', 'Review is required')
        return cleaned_data

    def clean_rating(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get("rating")

        if int(rating) > 5:
            self.add_error('rating', 'You can choose between 1 and 5')
        return cleaned_data
