from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('',views.home,name="home"),
    path('survey/', views.survey_view, name='survey'),  # Map the root URL to the 'home'
    path('surveyhome/',views.surveyhome, name="surveyhome"),
    path('understandingMH/',views.card1, name="understandingMH"),
    path('MHdisorders/',views.card2, name="MHdisorders"),
    path('factorsaffMH/',views.card3, name="factorsaffMH"),
    path('impMHaws/',views.card4, name="impMHaws"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('user-details/', views.user_details, name='user_details'),
    path('wellness/', views.wellness , name="wellness")
    ]
