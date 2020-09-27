from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from .forms import createuserform
def index(request):
    return  render(request,'index.html')

def register(request):
    if request.method=="POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        user_type = request.POST['user_type']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        password = request.POST['password']
        
        # user = User.objects.create_user(username=first_name,last_name=last_name,email=email,password=password)
        # user.userprofile.phone_number= phone_number
        # user.userprofile.gender= gender
        # user.userprofile.user_type= user_type
        # user.userprofile.address= address
        # user.userprofile.city= city
        # user.userprofile.state= state
        # user.userprofile.pincode= pincode
        # # user.save()
        # user = User.objects.get(pk=user_id)
        # print(user)
        # user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
        # user.profile = (phone_number=phone_number,gender=gender,user_type=user_type,address=address,city=city,state=state,pincode=pincode)
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
        else:
            inv = "invalid username and password"
            return render(request,'login.html',{'inv' : inv })
            inv = None
    else :
        inv = None
        return render(request,'login.html',{'inv' : inv})
def logout(request):
    auth.logout(request)
    return redirect(index)