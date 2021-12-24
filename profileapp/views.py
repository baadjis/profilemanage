

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect, reverse



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.core.exceptions import  ValidationError


from django.views import View

from profileapp.forms import CreationForm, ProfileForm
from profileapp.models import Profile


class RegisterView(View):

    def get(self, request):
        form = CreationForm()
        return render(request, 'profileform.html', {'form': form, 'title': 'Register'})

    def post(self, request):
        form = CreationForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect(reverse('accounts:login'))
        print("not valid")
        return render(request, 'profileform.html', {'form': form, 'title': 'Register'})


class LoginView(View):
    def get(self, request):
        return render(request, 'profileform.html', {'form': AuthenticationForm(), 'title': 'Login'})

    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("valide")
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            print(user)
            if user is None:
                print("none")
                return render(
                    request,
                    'profileform.html',
                    {'form': form, 'title': 'Login'}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'profileform.html',
                    {'form': form, 'title': 'Login'}
                )
            login(request, user)

            return redirect(reverse('accounts:profile'))
        else:
            print("invalid")
            args = {'form': form, 'title': 'Login'}
            return render(request, 'profileform.html', args)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        print(user)
        profile = get_object_or_404(Profile, user=user)
        pro= Profile.objects.filter(user=user).first()
        form = ProfileForm(instance=profile)
        context = {
            'user': pro,
            'title': 'Profile',
            'form': form
        }

        return render(request, 'profile.html', context)

    def post(self, request):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        pro=Profile.objects.filter(user=user).first()
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            print("valid")
            form.save()

            return HttpResponseRedirect(reverse('accounts:profile'))
        print("invalid")
        return render(request, 'profile.html', {
            'form': form,
            'title': 'profile',
            'user':pro

        })


def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/')