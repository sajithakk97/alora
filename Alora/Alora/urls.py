"""Alora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from event import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index,name='index'),
    path('register',views.Register,name='register'),
    path('login',views.Login,name='login'),
    path('profile',views.Profile,name='profile'),
    path('edit',views.Edit,name='edit'),
    path('user_home',views.User_home,name='user_home'),
    path('password_reset',views.Password_reset_request,name='password_reset'),
    path('verify_otp',views.Verify_otp,name='verify_otp'),
    path('set_new_password',views.Set_new_password,name='set_new_password'),
    path('book',views.Book_hall,name='book'),
    path('logout',views.Logout,name='logout'),
    path('view_user_booking',views.View_user_booking,name='view_user_booking'),
    path('set_payment_status/<int:id>',views.Set_payment_status,name='set_payment_status'),
    path('cash_pay/<int:id>',views.Cash_pay,name='cash_pay'),
    path('service',views.Service,name='service'),
    path('about',views.About,name='about'),
    path('gallery',views.Gallery,name='gallery'),
    path('testimonials',views.Testimonial,name='testimonial'),
   
    




    #admin...........
    path('view_user',views.View_user,name='view_user'),
    path('admin_home',views.Admin_home,name='admin_home'),
    path('add_hall',views.Add_hall,name='add_hall'),
    path('view_hall',views.View_hall,name='view_hall'),
    path('delete_hall/<int:id>',views.Delete_hall,name='delete_hall'),
    path('add_food',views.Add_food,name='add_food'),
    path('view_food',views.View_food,name='view_food'),
    path('delete_food/<int:id>',views.Delete_food,name='delete_food'),
    path('view_decoration',views.View_decoration,name='view_decoration'),
    path('add_decoration',views.Add_decoration,name='add_decoration'),
    path('delete_decoration/<int:id>',views.Delete_decoration,name='delete_decoration'),
    path('view_booking',views.View_booking,name='view_booking'),
    path('set_status/<int:id>',views.set_status,name='set_status'),
    
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
