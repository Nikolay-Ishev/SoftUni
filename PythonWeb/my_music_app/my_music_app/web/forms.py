from django import forms
from my_music_app.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': "Username",
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': "Email",
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }
            )
        }


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'img_url', 'price')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Album name",
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': "Artist",
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'img_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            )
        }


class DetailsAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            # deletes the model
            self.instance.delete()
            return self.instance

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'img_url', 'price')


class DetailsProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            # deletes the model
            self.instance.delete()
            # deletes all the expenses
            Album.objects.all().delete()
            return self.instance

    class Meta:
        model = Profile
        fields = ()
