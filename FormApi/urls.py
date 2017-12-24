from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^$',views.Login,name="login"),
	url(r'^logout/',views.Logout,name="logout"),
    url(r'^Sendmail/',views.Sendmail,name="Sendmail"),
    url(r'^/ViewDatabase/',views.ViewDatabase,name="ViewDatabase"),
    url(r'^/FillData/',views.FillData,name="FillData"),

]