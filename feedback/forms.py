from django import forms
from .models import Feedback, MenuItem

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['food', 'cleanliness', 'service_quality', 'menu_variety', 'rating', 'comments']

    # Override fields to populate choices dynamically
    cleanliness = forms.ChoiceField(choices=Feedback.FOOD_CHOICES)
    service_quality = forms.ChoiceField(choices=Feedback.FOOD_CHOICES)
    menu_variety = forms.ChoiceField(choices=Feedback.FOOD_CHOICES)

    # You can also dynamically generate the menu items here, but it will be done automatically by the form's `ModelChoiceField`.
    food = forms.ModelChoiceField(queryset=MenuItem.objects.all(), empty_label="Select Food Item")
