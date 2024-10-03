from typing import Any
from django.contrib.auth import authenticate,login
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import LoginForm

class AuthLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        print("Form valid.")
        user = form.get_user()
        print(user)
        login(self.request,user)
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        print("form_invalid: Form errors:", form.errors)
        response = super().form_invalid(form)
        return response
    
    def dispatch(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('client-dashboard')
        
        return super().dispatch(request,*args,**kwargs)
    
    
    