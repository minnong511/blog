# 장고 함수인 path

from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name = 'post_list'),
]
# 구성 urlpatterns = [
#   path(주소 , 보여줄 뷰 , 이름 )
# 이름 붙이는 거 상당히 중요하다 아시겠아요?
# ]
# 여기서는 html