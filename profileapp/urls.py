
from django.urls import  re_path
from . import views

app_name = 'ProfileApp'
urlpatterns = [
  re_path('^register/$', views.RegisterView.as_view(), name='register'),
  re_path('^login/$', views.LoginView.as_view(), name='login'),
  re_path('^profile/$', views.ProfileView.as_view(), name='profile'),
  re_path('^logout/$',views.logout_view,name='logout')

]
  