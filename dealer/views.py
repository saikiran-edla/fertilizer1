from django.shortcuts import render,redirect
from dealer.models import sregistration,Product
from django.contrib import messages
# Create your views here.
def sreg(request):
    return render(request,'seller reg.html')
def register(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        sregistration(Name=Name,Mobile=Mobile,Email=Email,Password=Password).save()
        messages.info(request,'registration is sucess')
        return redirect('sreg')
    else:
        return render(request,'seller reg.html')

def login(request):
    try:
        if request.session['suser']:
            return render(request,'dealerhome.html')
        else:
            return render(request,'sellerlogin.html')
    except KeyError:
        return render(request,'sellerlogin.html')

def validate(request):
    Email = request.POST['email']
    Password = request.POST['password']
    try:
        sregistration.objects.get(Email=Email,Password=Password)
        request.session['suser'] = Email
        res = sregistration.objects.filter(Email=Email)
        return render(request,'dealerhome.html',{'data':res})
    except:
        messages.info(request,'invalid User')
        return redirect('slogin')

def logout(request):
    try:
        del request.session['suser']
        return redirect('slogin')
    except KeyError:
        return redirect('slogin')

def shome(request):
    return request(request,'dealerhome.html')

def d_info(request):
    Email = request.session['suser']
    res = sregistration.objects.filter(Email=Email)
    return render(request,'Dealerinfo.html',{'data':res})

def addproduct(request):
    return render(request,'addproduct.html')
def addp(request):
    Email = request.session['suser']
    Pname = request.POST['pname']
    Pprice = request.POST['pprice']
    Pdesc = request.POST['pdesc']
    Pimage = request.FILES['pimage']
    Product(Email=Email,Pname=Pname,Pprice=Pprice,Pdesc=Pdesc,Pimage=Pimage).save()
    messages.info(request,'Product added sucessfully')
    return redirect('addproduct')
def display(request):
    Email = request.session['suser']
    res = Product.objects.filter(Email=Email)
    return render(request,'diaplay.html',{'data':res})


