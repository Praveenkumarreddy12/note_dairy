from django.urls import path
from . import views

urlpatterns = [
    # ... existing paths ...
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='log_in'),
    path('my-page/', views.MyPageView.as_view(), name='my_page'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
    path('page/<int:page_id>/', views.view_page_details, name='view_page_details'),
    path('forget-password/', views.forget_password, name='forget_password'),
    path('security-questions/', views.security_questions, name='security_questions'),
]
