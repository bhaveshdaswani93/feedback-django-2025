from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import FormProfile
from .models import Profile

# Create your views here.
def file_upload_util(file):
  with open('temp/image.jpg', "wb+") as dest:
    for chunk in file.chunks():
      dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = FormProfile()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        form = FormProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile(image=request.FILES['image'])
            profile.save()
            # file_upload_util(request.FILES['image'])
            return HttpResponseRedirect('/profiles')  
        
        return render(request, "profiles/create_profile.html", {
            "form": form
        })
        # file_upload_util(request.FILES['image'])