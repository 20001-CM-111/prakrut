from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import authenticate,login
from .models import *
from django.http import HttpResponse
from django.template import loader
current_user=''
def CreateAccount(request):
    global current_user
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            current_user=request.POST.get(form.Meta.fields[0])
            obj=Userdata()
            obj.user = User.objects.get(username=current_user)
            c=request.POST.get('Select')
            if(c=='Customer'):
                obj.Status='Customer'
                obj.save()
                messages.success(request,"Welcome "+request.POST.get(form.Meta.fields[0])+" ! Login to continue..")
                return redirect('/')
            else:
                obj.Status = 'Farmer'
                obj.save()
                messages.success(request,"Welcome "+request.POST.get(form.Meta.fields[2])+" ! Login to continue..")
                return redirect('/FarmerForm')
    context={'form':form}
    return render(request,'CreateAccount.html',context)
def Login(request):
    boolean=request.POST.get('Account')
    if boolean==True:
        return redirect('/CreateAccount')
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Hello "+name+" !")
            return redirect('/Home')
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect('/')
    return render(request,'Login.html')
def Home(request):
    return render(request,'Home.html')
def Form(request):
    global current_user
    if request.method=='POST':
        q=request.POST.getlist('Veg')
        for i in q:
            h=Product()
            h.product=i
            h.user=str(current_user)
            h.name=Vegetable.objects.get(Name=i)
            h.save()
        return redirect("/Price")
    return render(request,'FarmerForm.html')
def ForgotPassword(request):
    return render(request,'ForgotPassword.html')
def Price(request):
    global current_user
    h = []
    for i in Product.objects.filter(user=current_user):
        h.append(Vegetable.objects.get(Name=i.product))
    template = loader.get_template('Price.html')
    context = {'mymembers': h}
    if request.method == 'POST':
        price = request.POST.getlist('prices')
        c = 0
        for i in h:
            if i.Name == 'Tomato': obj = Tomato()
            elif i.Name == 'Okra': obj = Okra()
            elif i.Name == 'Brinjal': obj = Brinjal()
            elif i.Name == 'Chillies': obj = Chillies()
            elif i.Name == 'Cabbage':obj = Cabbage()
            elif i.Name == 'RunnerBeans':obj = RunnerBeans()
            elif i.Name == 'GreenBeans':obj = GreenBeans()
            elif i.Name == 'Cauliflower': obj = Cauliflower()
            elif i.Name == 'Capsicum': obj = Capsicum()
            elif i.Name == 'DrumStick': obj = DrumStick()
            elif i.Name == 'Spinach':obj = Spinach()
            elif i.Name == 'Amaranthus':obj = Amaranthus()
            elif i.Name == 'Coriander':obj = Coriander()
            elif i.Name == 'CurryLeaves': obj = CurryLeaves()
            elif i.Name == 'IvyGourd': obj = IvyGourd()
            elif i.Name == 'RidgeGourd': obj = RidgeGourd()
            elif i.Name == 'BitterGourd':obj = BitterGourd()
            elif i.Name == 'BottleGourd':obj = BottleGourd()
            elif i.Name == 'SnakeGourd':obj = SnakeGourd()
            elif i.Name == 'SpineGourd': obj = SpineGourd()
            elif i.Name == 'YellowCucumber': obj = YellowCucumber()
            elif i.Name == 'Potato': obj = Potato()
            elif i.Name == 'Sweetpotato':obj = Sweetpotato()
            elif i.Name == 'Ginger':obj = Ginger()
            elif i.Name == 'Taro':obj = Taro()
            elif i.Name == 'Carrot': obj = Carrot()
            elif i.Name == 'Radish':obj = Radish()
            elif i.Name == 'Beetroot':obj = Beetroot()
            elif i.Name == 'Onion':obj = Onion()
            else:obj=Garlic()
            obj.Price = price[c]
            obj.user = current_user
            obj.save()
            c = c + 1
        return redirect('/')
    return HttpResponse(template.render(context, request))




# Create your views here.
