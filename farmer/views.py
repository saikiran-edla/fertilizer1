from django.shortcuts import render,redirect
from farmer.models import fregistration
from dealer.models import sregistration,Product
from django.contrib import messages
# Create your views here.
def home(request):
    res = Product.objects.all()
    return render(request,'home.html',{'data':res})
def product(request):
    res = Product.objects.all()
    return render(request,'products.html',{'data':res})
def freg(request):
    return render(request,'customer.html')
def register(request):
    if request.method == 'POST':
        Fname = request.POST.get('fname')
        Lname = request.POST.get('lname')
        Mobile = request.POST.get('mobile')
        Email = request.POST.get('email')
        State = request.POST.get('state')
        District = request.POST.get('district')
        Mandal = request.POST.get('mandal')
        Village = request.POST.get('village')
        Aadhaar = request.POST.get('aadhaar')
        Passbook = request.POST.get('passbook')
        Password = request.POST.get('password')
        Repassword = request.POST.get('repassword')
        if Password != Repassword:
            messages.info(request,'Password doesnot match')
            return redirect('freg')
        else:
            fregistration(Fname=Fname,Lname=Lname,Mobile=Mobile,Email=Email,State=State,District=District,Mandal=Mandal,Village=Village,Aadhaar=Aadhaar,Passbook=Passbook,Password=Password,Repassword=Repassword).save()
            messages.info(request,'Your registration is sucess')
            return redirect('freg')
    else:
        return render(request,'customer.html')

def flogin(request):
    try:
        if request.session['fuser']:
            return render(request,'farmerhome.html')
        else:
            return render(request,'farmer login.html')
    except KeyError:
        return render(request,'farmer login.html')
def fhome(request):
    Email = request.session['fuser']
    res = fregistration.objects.filter(Email=Email)
    return render(request,'farmerhome.html',{'data':res})

def validate(request):
    Email = request.POST['email']
    Password = request.POST['password']
    try:
        fregistration.objects.get(Email=Email,Password=Password)
        request.session['fuser'] = Email
        res = fregistration.objects.filter(Email=Email)  
        return render(request,'farmerhome.html',{'data':res})
    except:
        messages.info(request,'invalied user')
        return redirect('flogin')

def logout(request):
    del request.session['fuser']
    return render(request,'farmer login.html')

def contactus(request):
    return render(request,'contactus.html')    
def fproduct(request):
    res = Product.objects.all()
    return render(request,'farmerproducts.html',{'data':res})
def f_info(request):
    Email = request.session['fuser']
    res = fregistration.objects.filter(Email=Email)
    return render(request,'farmerinfo.html',{'data':res})