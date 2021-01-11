"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import index , welcome , template_test , hello
# from을 이용해서 뷰에 관한 정보를 .views 에서 끌어온다 -> 내가 추가한 뷰는 여기 전부 끌어와야 한다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',welcome),
    path('',index),
    path('test_view/',template_test),
    path('A',hello)
    # path(주소,뷰,주소의 별명)
    # 여기서 localhost:8000/welcome 하면 그에 해당하는 정보들이 나오게 된다
]
