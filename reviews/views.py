from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# Create your views here.

def reviews(request):
  if request.method == 'POST':
    print(request.POST)
    form = ReviewForm(request.POST)
    
    if form.is_valid():
      print(form.cleaned_data)
      review = Review(
        user_name=form.cleaned_data['user_name'],
        review=form.cleaned_data['review'],
        rating=form.cleaned_data['rating']
      )
      review.save()
      return HttpResponseRedirect('/reviews/thank_you')
  else:
    form = ReviewForm()

  return render(request, 'reviews/review.html', {
   'form': form
  })

def thank_you(request):
  return render(request, 'reviews/thank_you.html')
