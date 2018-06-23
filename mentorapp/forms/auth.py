from django import forms
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import ipdb
from django.views.generic import CreateView


class SignUpForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class LoginFormView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(
            request,
            template_name='login_form.html',
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            ipdb.set_trace()
            if user is not None:

                login(request,user)
                return redirect('mentorApp:college_html')
            else:
                return redirect('mentorApp:SignUpform')


class SignUpFormView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name="signup_form.html",
            context={
                'form': SignUpForm()
            }
        )

    def post(self, request, *args, **kwargd):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(**form.cleaned_data)
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('mentorApp:college_html')
            else:
                return redirect('mentorApp:loginForm')


class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect('mentorApp:loginForm')