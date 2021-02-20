from django.urls import path
from farmer import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.product,name='product'),
    path('freg',views.freg,name='freg'),
    path('register',views.register,name='register'),
    path('validate',views.validate,name='validate'),
    path('fhome',views.fhome,name='fhome'),
    path('flogin',views.flogin,name='flogin'),
    path('logout',views.logout,name='logout'),
    path('contactus',views.contactus,name='contactus'),
    path('fproduct',views.fproduct,name='fproduct'),
    path('f_info',views.f_info,name='f_info')
]