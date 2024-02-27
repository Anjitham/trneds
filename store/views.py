from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from store.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from store.models import Product

# lh:8000/register/
# get,post
# form_class:registrationForm
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"login.html",{"form":form})
        
# lh:8000/sigin
# get,post
# form_class:loginform
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("index")
        messages.error(request,"Invalid credentials")
        return render(request,"login.html",{"form":form})


# class IndexView(TemplateView):
#     template_name="index.html"
    
class IndexView(View):

        def get(self,request,*args,**kwargs):
            qs=Product.objects.all()
            return render(request,"index.html",{"data":qs})
        
class ProductDetailview(View):

        def get(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            qs=Product.objects.get(id=id)
            return render (request,"product_detail.html",{"data":qs})
        
class HomeView(TemplateView):
 
     template_name="base.html"