from django.shortcuts import render, redirect

# Create your views here.
from my_music_app.web.forms import CreateProfileForm, CreateAlbumForm, DetailsAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from my_music_app.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()
    # budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'albums': albums,
        # 'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def create_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DetailsAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DetailsAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DetailsAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DetailsAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
    }
    return render(request, 'delete-album.html', context)


def details_profile(request):
    profile = get_profile()
    albums = len(Album.objects.all())

    context = {
        'profile': profile,
        'albums': albums,
        # 'budget_left': budget_left,
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
