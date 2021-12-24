
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.widgets import EmailInput

from profileapp.models import Profile


class CreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=EmailInput)
    bio = forms.Textarea()

    class Meta:
        model = Profile
        fields = [

            'email',

            'bio'

        ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['bio'].require=False
        try:
            self.fields['email'].initial = self.instance.user.email
        except User.DoesNotExist:
            pass

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()

        bio = cleaned_data.get("bio")
        


        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )
    def save(self, *args, **kwargs):
        """
        Update the primary email address on the related User object as well. 
        """
        u = self.instance.user
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(ProfileForm, self).save(*args,**kwargs)
        return profile