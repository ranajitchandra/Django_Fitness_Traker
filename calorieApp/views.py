from django.shortcuts import render, redirect, get_object_or_404
from calorieApp.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.

def signupPage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        img=request.FILES.get('image')
        
        if password==cpassword:
            user=Custom_user.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            
            user.gender=gender
            user.age=age
            user.height=height
            user.weight=weight
            user.image=img
            user.save()
            if gender=="male":
                result=66.47+(13.75*float(weight))+(5.003*float(height))-(6.755*float(age))
                calorieInfo.objects.create(user=user, result=result)  
            elif gender=="female":
                result=65.51+(9.563*float(weight))+(1.850*float(height))-(4.676*float(age))
                calorieInfo.objects.create(user=user, result=result)
            
            return redirect('signinPage')
     
    return render(request, 'signup.html')


def signinPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_login = authenticate(username=username, password=password)
        if user_login:
            login(request, user_login)
            return redirect('dashboard')        
        

    return render(request, 'signin.html')


def logoutPage(request):
    logout(request)
    return redirect('signinPage')



@login_required
def dashboard(request):
    calinfo =get_object_or_404(calorieInfo, user=request.user)
    foodinfo =foods.objects.filter(user=request.user)

    sumcalorie=0
    for i in foodinfo:
        sumcalorie+=i.consume
    print(calinfo)
    print(sumcalorie)
    result = float(calinfo.result) - sumcalorie
    context = {
        'calinfo' : calinfo,
        'foodinfo' : foodinfo,
        'result' : result,
    }

    return render(request, 'dashboard.html', context)


@login_required
def addfood(request):
    if request.method=="POST":
        name=request.POST.get('name')
        calories=request.POST.get('calories')
        date=request.POST.get('date')
        foods.objects.create(user=request.user, name=name, consume=calories, date=date)
        return redirect('dashboard')

    return render(request, 'addfood.html')


