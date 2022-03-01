import os

from django import forms

from expenses_tracker.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            # deletes the model
            self.instance.delete()
            # deletes all the expenses
            Expense.objects.all().delete()
            # deletes img file
            image_path = self.instance.profile_image.path
            os.remove(image_path)

            return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'image': 'Link to Image',
        }


class DeleteExpenseForm(forms.ModelForm):
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
        model = Expense
        fields = ('title', 'description', 'image', 'price')
