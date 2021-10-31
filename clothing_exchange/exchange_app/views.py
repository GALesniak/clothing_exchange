from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Institution, Donation
from accounts.models import CustomUser

from django.contrib.auth import authenticate, login, logout


class LandingPage(View):
    def get(self, request):
        all_bags = Donation.objects.all().count()
        bag_qty = []
        for _ in range(all_bags):
            bag_qty.append(Donation.objects.all()[_].quantity)
        organization_qty = Institution.objects.all().count()

        foundations = Institution.objects.filter(type=1).all()
        non_gov = Institution.objects.filter(type=2).all()
        people = Institution.objects.filter(type=3).all()

        return render(request, 'exchange_app/index.html',
                      {'bag_qty': sum(bag_qty),
                       'organization_qty': organization_qty,
                       'foundations': foundations,
                       'non_gov': non_gov,
                       'people': people,
                       })


class AddDonation(View):
    def get(self, request):
        return render(request, 'exchange_app/form.html')


class Login(View):
    def get(self, request):
        return render(request, 'exchange_app/login.html')

    def post(self, request):

        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        print(CustomUser.objects.filter(email=email))

        user = authenticate(email=email, password=password)
        print(user)
        if user:
            login(self.request, user)
            first_name = "udało się"
            return render(request, 'exchange_app/index.html', {'first_name': first_name})
        else:
            first_name = "nie udało się"
            return render(request, 'exchange_app/index.html', {'first_name': first_name})















class Register(View):
    def get(self, request):
        return render(request, 'exchange_app/register.html')

    def post(self, request):
        if request.POST.get('password') == request.POST.get('password2'):
            user = CustomUser.objects.create(

                first_name=request.POST.get("name"),
                last_name=request.POST.get("surname"),
                email=request.POST.get("email"),
                password=request.POST.get("password")
            )
            user.save()
            return redirect('login_page')
        else:
            return redirect('register_page')
