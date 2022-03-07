from django.shortcuts import render, redirect

from petstagram.main.forms import CreatePetPhotoForm, EditPetPhotoForm, DeletePetPhotoForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto


def create_pet_photo(request):
    if request.method == 'POST':
        form = CreatePetPhotoForm(request.POST, request.FILES, instance=PetPhoto(user_profile=get_profile()))
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreatePetPhotoForm()
    context = {
        'form': form,
    }
    return render(request, 'photo_create.html', context)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    # pet_photo = PetPhoto.objects.get(id=pk)

    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


def edit_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetPhotoForm(request.POST, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPetPhotoForm(instance=pet_photo)

    context = {
        'form': form,
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_edit.html', context)


def delete_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePetPhotoForm(request.POST, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeletePetPhotoForm(instance=pet_photo)

    context = {
        'form': form,
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_delete.html', context)