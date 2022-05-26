from TENNIS_APP import views
from django.urls import path

urlpatterns = [
    path('',views.home_view,name="home"),
    path('about/',views.about_view,name="about"),
    path('contact/',views.contact_view,name="contact"),
    path('footer/',views.footer_view,name="footer"),
    
    
    path('tennis/',views.tennis_view,name="tennis"),
    path('tennis-info/',views.tennis_info_view,name="tennis_info"),
    
    path('online-booking/',views.online_booking_view,name="onlinebooking"),
    
    path('booking-display/',views.display_booking_view,name="display"),
    
    
    
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    
    path('email/', views.email_view, name='email'),
    

]