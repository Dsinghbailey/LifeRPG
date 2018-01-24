"""LifeRPG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from DesktopApp import views as core_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^contact', core_views.contact, name='contact'),
    url(r'^about',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^register', core_views.register_view, name='register'),
    url(r'^login', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout', core_views.logout_view, name='logout'),
    url(r'^create_profile', core_views.create_profile, name='create_profile'),
    url(r'^tutorial', core_views.tutorial, name='tutorial'),
    url(r'^profile', core_views.profile, name='profile'),
    url(r'^levelup', core_views.levelup, name='levelup'),
    url(r'^missions', core_views.missions, name='missions'),
    url(r'^admin/', admin.site.urls),
]
