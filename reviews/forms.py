from django import forms
from .models import Review

"""
class ReviewForm(forms.Form):
  user_name = forms.CharField(label='Your Name', max_length=100, error_messages={
    'required': 'Your name must not be empty',
    'max_length': 'Please enter a shorter name'
  })
  review = forms.CharField(label='Your Review', widget=forms.Textarea, error_messages={
    'required': 'Your review must not be empty'
  })
  rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5, error_messages={
    'required': 'Please enter a rating',
    'min_value': 'Please enter a rating of 1 or higher',
    'max_value': 'Please enter a rating of 5 or lower'
  })
  """
  
class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ('user_name', 'review', 'rating')
    labels = {
      'user_name': 'Your name',
      'review': 'Your Review',
      'rating': 'Please Enter rating'
    }
    error_messages = {
      'user_name': {
        'required': 'User name is required',
        'max_length': 'Please enter a shorter name'
      },
      'review': {
        'required': 'Please enter a review'
      },
      'rating': {
        'required': 'Please enter a rating',
        'min_value': 'Please enter a rating of 1 or higher',
        'max_value': 'Please enter a rating of 5 or lower'
      }
    }
    
  
    
  
  