from datetime import date
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *


def logout_view(request):
    logout(request)
    return redirect('index')


class IndexView(View):
    template_name = 'login/index.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class HomeView(View):
    template_name = 'login/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.filter(user__username=request.user.username).first()
            self.context['profile'] = profile
        return render(request, self.template_name, self.context)


class LoginView(View):
    template_name = 'login/login.html'
    context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        login_data = request.POST.dict()
        log = login_data.get("log")
        pwd = login_data.get("pwd")

        existing_user = Profile.objects.filter(user__username=log).first()
        if not existing_user:
            self.context['status'] = 'non-existent'
        else:
            user = authenticate(request, username=log, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, self.template_name, self.context)


class RegisterView(View):
    template_name = 'login/register.html'
    context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        login_data = request.POST.dict()
        first_name = login_data.get("user_first_name")
        last_name = login_data.get("user_last_name")
        city = login_data.get("mepr-address-city")
        country = login_data.get("mepr-address-country")
        email = login_data.get("user_email")
        password = login_data.get("mepr_user_password")
        months = login_data.get("months")

        existing_user = Profile.objects.filter(user__username=email).first()
        if existing_user:
            self.context['registered'] = 'exists'
        else:
            new_user = User.objects.create_user(username=email, email=email, password=password)
            expiration_date = date.today() + relativedelta(months=+ int(months))
            new_profile = Profile(
                user=new_user,
                nombre=first_name,
                apellido=last_name,
                ciudad=city,
                pais=country,
                email=email,
                fecha_fin=expiration_date).save()
            self.context['registered'] = 'success'
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, self.template_name, self.context)
