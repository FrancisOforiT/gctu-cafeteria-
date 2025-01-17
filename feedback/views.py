from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feedback, MenuItem
from .forms import FeedbackForm

@login_required
def index(request):
    menus = MenuItem.objects.all()
    feedback_submitted = False  # Default state for the success message

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Assign the logged-in user
            feedback.save()
            feedback_submitted = True  # Set flag to show the success message
        else:
            messages.error(request, "There was an error submitting your feedback. Please try again.")

    else:
        form = FeedbackForm()

    context = {
        'menus': menus,
        'form': form,
        'cleanliness_choices': Feedback.FOOD_CHOICES,
        'service_quality_choices': Feedback.FOOD_CHOICES,
        'menu_variety_choices': Feedback.FOOD_CHOICES,
        'feedback_submitted': feedback_submitted,  # Pass success flag to the template
    }

    return render(request, 'index.html', context)
