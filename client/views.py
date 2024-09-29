from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import UserModel
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        print("Reach to endpoint.")
        form = RegisterForm(request.POST)
        if form.is_valid():
            #extracting files from form.
            user_name = form.cleaned_data['user_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')

            try:
                UserModel.objects.create_user(user_name = user_name,
                                          email_address = email_address,
                                          phone_number = phone_number,
                                          password = password,
                                          latitude = latitude,
                                          longitude = longitude
                                          )
                print("User created ! Yayyyy.")

                auth_user = authenticate(email_address = email_address,password = password)
                if auth_user is not None:
                    login(request, auth_user)
                    return redirect('client-dashboard')
                else:
                    return redirect('login')
            except Exception as e:
                print(e)

        else:
            print("Not valid !")
    else:
        form = RegisterForm()

    return render(request, 'register.html',{'form':form})

def test(request):
    return render(request,"test.html")


@login_required
def client_dashboard(request):
    return render(request,'dashboard/dashboard.html')