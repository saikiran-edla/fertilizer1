from django.urls import path
from dealer import views
urlpatterns = [
    path('',views.sreg,name='sreg'),
    path('register',views.register,name='register'),
    path('slogin',views.login,name='slogin'),
    path('validate',views.validate,name='validate'),
    path('logout',views.logout,name='logout'),
    path('shome',views.shome,name='shome'),
    path('dinfo',views.d_info,name='dinfo'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('addp',views.addp,name='addp'),
    path('display',views.display,name='display')
]