from datetime import date

from django.forms import ModelForm

from .models import Review, Stay


class StayForm(ModelForm):
    class Meta:
        model = Stay
        fields = ['owner', 'provider', 'start_date', 'end_date', 'pets']

    def clean_start_date(self):
        now = date.today()
        chosen_date = self.cleaned_data['start_date']
        if chosen_date and chosen_date < now:
            self.add_error('start_date', 'Start date should be a valid date')
        return chosen_date

    def clean_end_date(self):
        now = date.today()
        start_date = self.cleaned_data['start_date']
        chosen_date = self.cleaned_data['end_date']
        if chosen_date and chosen_date < now and chosen_date < start_date:
            self.add_error('end_date', 'End date should be greater than start date.')
        return chosen_date

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
        fields = ['stay', 'review', 'rating']

    def clean_stay(self):
        stay = self.cleaned_data.get('stay')
        if not stay:
            self.add_error('stay', 'Stay is required')
        return stay

    def clean_review(self):
        review = self.cleaned_data.get('review')
        if review and len(review) < 1:
            self.add_error('review', 'Review is required')
        return review

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")

        if int(rating) > 5:
            self.add_error('rating', 'You can choose between 1 and 5')
        return rating
