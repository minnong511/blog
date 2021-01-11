"""
ASGI config for djangoProject1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
# Asynchronous Server Gateway Interface
# 비동기 웹서버와 애플리케이션을 위한 파이썬 표준 ASGI
# wsgi 는 단일 처리만 가능한 동기 호출 방식 -> 웹 소켓이나 긴 대기시간을 갖는 http 연결에 적합하지 않음
# ASGI는 WSGI의 상위 호환 , 파이썬과 애플리케이션을 이어주는 API , 표준 인터페이스


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')

application = get_asgi_application()
