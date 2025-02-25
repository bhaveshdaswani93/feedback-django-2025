from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView
from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(View):
  def get(self, request):
    form = ReviewForm()
    return render(request, 'reviews/review.html', {
      'form': form
    })
    
  def post(self, request):
    form = ReviewForm(request.POST)
    
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/reviews/thank_you')
      
    return render(request, 'reviews/review.html', {
      'form': form
    })



# def reviews(request):
#   if request.method == 'POST':
#     # print(request.POST)
#     # review = Review.objects.get(pk=1)
#     form = ReviewForm(request.POST)
    
#     if form.is_valid():
#       print(form.cleaned_data)
#       # review = Review(
#       #   user_name=form.cleaned_data['user_name'],
#       #   review=form.cleaned_data['review'],
#       #   rating=form.cleaned_data['rating']
#       # )
#       # review.save()
#       form.save()
#       return HttpResponseRedirect('/reviews/thank_you')
#   else:
#     form = ReviewForm()

#   return render(request, 'reviews/review.html', {
#    'form': form
#   })

class ThankYouView(TemplateView):
  template_name = "reviews/thank_you.html"
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add data to the context here if needed
        return context
  
  """
  def get(self, request):
    return render(request, 'reviews/thank_you.html')
  """

class ReviewListView(ListView):
  template_name = "reviews/reviews.html"
  model = Review
  context_object_name = 'reviews'

  # def get_queryset(self):
  #   return super().get_queryset().filter(rating__gt=3)
  
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   reviews = Review.objects.all()
  #   context['reviews'] = reviews
  #   return context

class ReviewDetailView(TemplateView):
  template_name = "reviews/review_detail.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    review = Review.objects.get(pk=kwargs['pk'])
    context['review'] = review
    return context