from django.conf import settings
from django.db import models
from django.utils import timezone

# 모델을 만들면 항상 DB에 저장할 수 있도록
# python manage.py makemigrations 파일명
# python manage.py migrate 파일명$  pip install django~=3.1.5

# OOP 객체지향프로그래밍 , 모델을 제작해서 모델을 정의하여 알아서 상호작용하도록 만든다

# 객체속성 , 행위는 메서드로 구현된다

# 클래스 Post 내부의 models.Model 은 포스트가 장고 모델임을 의미한다. , 포스트가 DB에 저장된다는 걸
# 알 수 있게 만든다

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey - 다른 모델에 대한 링크를 의미한다
    title = models.CharField(max_length=200)
    # models.Charfield - 글자 수가 제한된 텍스트를 정의할 때 사용한다
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title