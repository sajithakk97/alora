from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import auth
from .models import User,User_details,Hall,Food,Decoration,Booking
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
import random
def Index(request):
    return render(request,'index.html')
def Register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        address=request.POST['address']
        username=request.POST['uname']
        password=request.POST['password']
        password2=request.POST['cpass']
        if(password==password2):
            if (User.objects.filter(email=email).exists()):
                error='Email is already in use'
                return render(request,'register.html',{'error':error})
            data=User.objects.create_user(username=username,email=email,first_name=name,password=password)
        else:
            msg='password do not match '
            return render(request,'register.html',{'message':msg})
        
        user=User_details.objects.create(phone_number=phone,gender=gender,address=address,user_id=data)
        data.save()
        return redirect('login')
    return render(request,'register.html')
def User_home(request):
    return render(request,'user_home.html')
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        admin_user=authenticate(request,username=username,password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return redirect('admin_home')
        user=authenticate(username=username,password=password)
        if  user is not None:
            login(request,user)
            return redirect('user_home')
        else:
            error='invalid credentials'
            return render(request,'login.html',{'error':error})
    else:
        return render(request,'login.html')
def Profile(request):
    data=User.objects.get(id=request.user.id)
    user=User_details.objects.get(user_id=data)
    print(data)
    return render(request,'profile.html',{'details':user})

def Edit(request):
    data=User_details.objects.get(user_id=request.user.id)
    if request.method=='POST':
        data.user_id.first_name=request.POST['name']
        data.user_id.email=request.POST['email']
        data.user_id.username=request.POST['uname']
        data.phone_number=request.POST['phone']
        data.address=request.POST['address']
        data.gender=request.POST['gender']
        data.user_id.save()
        data.save()
        return redirect('profile')
    return render(request,'edit.html',{'details':data})
def send_otp(email):
    otp=random.randint(100000,999999)
    send_mail('your otp code ',f'your otp code is {otp}','sajitharahman1997@gmail.com',[email],fail_silently=False,)
    return otp

def Password_reset_request(request):
    if request.method=='POST':
        email=request.POST['email']
        try:
            user=User.objects.get(email=email)
            otp=send_otp(email)
            context={
                'email':email,
                'otp':otp
            }
            return render(request,'verify_otp.html',context)
        except User.DoesNotExist:
            messages.error(request,'email address not found')
    else:
        return render(request,'password_reset.html')
    return render(request,'password_reset.html')

def Verify_otp(request):
    if request.method=='POST':
        email=request.POST.get('email')
        otpold=request.POST.get('otp')
        otp=request.POST.get('otp1')
        if otpold==otp:
            context={'otp':otp,
                     'email':email}
            return render(request,'new_password.html')
        else:
            messages.error(request,'Invalid otp')
    return render(request,'verify_otp.html')
def Set_new_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        new_password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if new_password==confirm_password:
            try:
                data=User.objects.get(email=email)
                data.set_password(new_password)
                data.save()
                messages.success(request,'password has been reset successfully')
                return redirect('login')
            except data.DoesNotExist:
                messages.error(request,'password doesnot match')
        return render(request,'new_password.html',{'email':email})
    return render(request,'new_password.html',{'email':email})

def Book_hall(request):
    hall = Hall.objects.all()
    food = Food.objects.all()
    decorations = Decoration.objects.all()
    user = User.objects.get(id=request.user.id)
    context = {
        'data': hall,
        'foods': food,
        'decoration': decorations
    }
    
    if request.method == 'POST':
        hall = request.POST.get('hall')
        food1 = request.POST.get('food1')  
        food2 = request.POST.get('food2')
        suggestion = request.POST.get('suggestion')
        date = request.POST.get('date')
        people_num = int(request.POST.get('people_num'))
        photography = request.POST.get('photography')  
        decoration = request.POST.get('decoration1')  
        decoration_model = request.POST.get('decoration_model')
        if not hall or not date or not people_num:
            return HttpResponse("Required fields are missing")

        hall_id = Hall.objects.get(id=hall)
        food_id = Food.objects.get(id=food2) if food2 else None
        decoration_id = Decoration.objects.get(id=decoration_model) if decoration_model else None
        total_cost = hall_id.price_per_day
        total_cost = hall_id.price_per_day
        if food1 == 'True' and food_id:
            total_cost += food_id.food_price * people_num
        if photography == 'True':
            total_cost += 10000
        if decoration == 'True' and decoration_model:
            total_cost += decoration_id.decoration_price 
        
        data = Booking.objects.create(
            customer_id=user,
            hall_id=hall_id,
            event_date=date,
            payment_status='pending',
            include_photography=photography ,
            include_food=food1 ,
            food=food_id,
            include_decoration=decoration ,
            decoration_model=decoration_id,
            suggestion=suggestion,
            total_cost=total_cost,
            number=people_num
        )
        data.save()
        return HttpResponse('success')
    
    return render(request, 'book.html', context)
def index1(request):
    return render(request,'base.html')







#admin........................
def Admin_home(request):
    return render(request,'admin_home.html')

def View_user(request):
    data=User_details.objects.all()
    return render(request,'view_user.html',{'details':data})

def View_hall(request):
    halls=Hall.objects.all()
    return render(request,'view_hall.html',{'data':halls})
def Add_hall(request):
    if request.method=='POST':
        name=request.POST['name']
        location=request.POST['location']
        capacity=request.POST['capacity']
        price=request.POST['price']
        desc=request.POST['description']
        image=request.FILES['image']
        hall=Hall.objects.create(name=name,
                                 location=location,
                                 capacity=capacity,
                                 price_per_day=price,
                                 description=desc,
                                 photo_url=image)
        hall.save()
        return redirect('view_hall')
    return render(request,'add_hall.html')
def Delete_hall(request,id):
    hall=Hall.objects.get(id=id)
    hall.delete()
    return redirect('view_hall')
def View_food(request):
    food=Food.objects.all()
    return render(request,'view_food.html',{'data':food})

def Add_food(request):
    if request.method=='POST':
        name=request.POST['name']
        image=request.FILES['img']
        price=request.POST['price']
        food=Food.objects.create(food_name=name,
                                 food_price=price,
                                 food_image=image)
        food.save()
        return redirect('view_food')
    return render(request,'add_food.html')
def Delete_food(request,id):
    food=Food.objects.get(id=id)
    food.delete()
    return redirect('view_food')

def View_decoration(request):
    decoration=Decoration.objects.all()
    return render(request,'view_decoration.html',{'data':decoration})

def Add_decoration(request):
    if request.method=='POST':
        image=request.FILES['img']
        price=request.POST['price']
        decoration_name=request.POST['decoration_name']
        decoration=Decoration.objects.create(decoration_price=price,
                                                decoration_image=image)
        decoration.save()
        return redirect('view_decoration')
    return render(request,'add_decoration.html')
def Delete_decoration(request,id):
    decoration=Decoration.objects.get(id=id)
    decoration.delete()
    return redirect('view_decoration')



    

        