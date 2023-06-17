from django import forms
from .models import UserProfile
from cloudinary.forms import CloudinaryFileField


class ProfileForm(forms.ModelForm):
    photo = CloudinaryFileField(
        options={
            'folder': 'profile_photos',
            'overwrite': True,
            'resource_type': 'image',
            'max_file_size': 5242880,  # 5MB
        },
        required=False  # Allow clearing the existing photo
    )

    class Meta:
        model = UserProfile
        fields = ['photo']
