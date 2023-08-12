"""
URL configuration for vlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from post import views as pos
from user import views as use


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', use.show_post, name='show_post'),
    path('signup/', use.signup, name='signup'),
    path('login/',use.login,name='login'),
    path('logout', use.logout,name='logout')
    

]
