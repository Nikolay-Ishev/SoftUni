from django.shortcuts import render, redirect

# Create your views here.
from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_nav_bars': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('error 401')
    pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def error_401(request):
    return render(request, '401_error.html')
