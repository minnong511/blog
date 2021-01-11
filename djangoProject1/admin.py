# admin.py는 모델을 관리자 페이지에 등록 해 관리할 수 있도록 하는 역할과,
# 관리자 페이지에서 보이는 내용의 변경,기능추가 등을 할 수 있도록 코드를 입력하는 파일입니다
# 초기에 만들게 된다면 (superuser)를 만들어야 한다.
# 명령어는 python manage.py createsuperuser
# 주의할 점은 비번치는 거 글자가 안보인다 (실제로 쳐지고 있음 ㅋㅋ)

from django.contrib import admin

# 여기에 당신의 모델을 입력하세요

from .models import Bookmark