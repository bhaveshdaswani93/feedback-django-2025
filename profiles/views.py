from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import FormProfile
from .models import Profile
from django.views.generic import CreateView, ListView

# Create your views here.
def file_upload_util(file):
  with open('temp/image.jpg', "wb+") as dest:
    for chunk in file.chunks():
      dest.write(chunk)


class ListProfileView(ListView):
    model = Profile
    template_name = 'profiles/list_profiles.html'
    context_object_name = 'profiles'

    # def get_queryset(self):
    #     return Profile.objects.all()

class CreateProfileView(CreateView):
    model = Profile
    fields = ['image']
    template_name = 'profiles/create_profile.html'
    success_url = '/profiles'

    # def form_valid(self, form):
    #     file_upload_util(self.request.FILES['image'])
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     return super().form_invalid(form)

# class CreateProfileView(View):
#     def get(self, request):
#         form = FormProfile()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = FormProfile(request.POST, request.FILES)
#         if form.is_valid():
#             profile = Profile(image=request.FILES['image'])
#             profile.save()
#             # file_upload_util(request.FILES['image'])
#             return HttpResponseRedirect('/profiles')  
        
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })
        # file_upload_util(request.FILES['image'])