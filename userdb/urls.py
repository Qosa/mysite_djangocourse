from django.conf.urls import url
from django.contrib import admin
from userdb import views

app_name = 'userdb'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.users,name='users2'),
    url(r'^formname/', views.form_name_view,name='formname'), 
]