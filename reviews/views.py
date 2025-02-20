from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def reviews(request):
  if request.method == 'POST':
    username = request.POST['username']
    print(username)
    return HttpResponseRedirect('/reviews/thank_you')

  return render(request, 'reviews/review.html')

def thank_you(request):
  return render(request, 'reviews/thank_you.html')
