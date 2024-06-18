"""EVotingBlockChain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from SmartVoting import views as mainView
from admins import views as admins
from users import views as usr
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name="index"),
    path("index/", mainView.index, name="index"),
    path("Adminlogin/",mainView.AdminLogin,name="AdminLogin"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),


    #adminviews
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path('RegisterUsersView/', admins.RegisterUsersView, name='RegisterUsersView'),
    path("PartiesRegisterActions/", admins.PartiesRegisterActions, name="PartiesRegisterActions"),
    path('DeleteParty/', admins.DeleteParty, name='DeleteParty'),
    path('AdminElectionsTurnOn/', admins.AdminElectionsTurnOn, name='AdminElectionsTurnOn'),
    path('VoteTurnOn/', admins.VoteTurnOn, name='VoteTurnOn'),
    path('VoteTurnOff/', admins.VoteTurnOff, name='VoteTurnOff'),
    path('AdminElectionsResults/', admins.AdminElectionsResults, name='AdminElectionsResults'),


    #User Views
    path("VoterRegistrations/", usr.VoterRegistrations, name="VoterRegistrations"),

    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("VoterPage/", usr.VoterPage, name='VoterPage'),
    path("VoterVoting/", usr.VoterVoting, name="VoterVoting"),
    # path("ECViewResults/", usr.ECViewResults, name='ECViewResults'),
    path("save_image/", usr.save_image, name="save_image"),
    path("ValidatePicandOTP/", usr.ValidatePicandOTP, name="ValidatePicandOTP"),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

