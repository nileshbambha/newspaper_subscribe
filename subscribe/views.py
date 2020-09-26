from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    return  render(request,'index.html')
def register(request):
    if request.method=="POST":
        name = request.POST['name']
        passwd = request.POST['password']
        user = User.objects.create_user(username=name,password=passwd)
        user.save()
        return redirect(index)
    else:
        return render(request,'register.html')
def login(request):
    if request.method =="POST":
        name = request.POST['email']
        passwd = request.POST['pass']
        user = auth.authenticate(username=name,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect(index)
    else :
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect(index)