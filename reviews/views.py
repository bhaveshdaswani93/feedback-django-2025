from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.

def reviews(request):
  if request.method == 'POST':
    print(request.POST['username'])
    username = request.POST['username']
    if username == "" or len(username) > 100:
      return render(request,'reviews/review.html', {
        'has_error': True
      })
    print(username)
    return HttpResponseRedirect('/reviews/thank_you')
  form = ReviewForm()
  return render(request, 'reviews/review.html', {
    'has_error': False
  })

def thank_you(request):
  return render(request, 'reviews/thank_you.html')
