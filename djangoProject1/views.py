# 뷰 - 글쓰기 페이지
# 화면이 나타나는 뷰 -> 템플릿이 있는 뷰
# 화면이 없는 뷰 -> 로그인 화면 같이 실시간으로 띄울 필요가 없는 경우
# AJAX 처럼 실시간 뷰와 같은 경우에도 화면이 없는 뷰가 있다다from django.shortcuts import render
# 화면이 있건 없건 뷰는 있어야 한다

from django.http import HttpResponse
from django.shortcuts import render

"""render는 템플릿을 불러온다"""

# 뷰 내용(함수,클래스)는 URL이 있으면 작동한다

# 함수형 : request를 매개변수로 받고(매겨변수 추가가능), 모양은 함수
# 내가 원하는대로 동작들을 설계하고 만들고 싶을 때

# 클래스형: CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고 상속받아서 사용한다.
# 장고의 제네릭 뷰를 많이 사용

# 함수형 뷰가 장고의 기준

# 페이지 만들 때마다 바뀌는 것이 다이나믹


    # 계산이나, 데이터베이스 조회 ,수정 , 등록
    # 응답 메시지를 만들어서 반환

# 문제 1
# 뷰의 이름은 : welcome -> 뷰의 이름은 곧 함수이름이 된다
# 뷰의 접속주소 : welcome/ -> urls 로 가라
# 내용은 : welcome django

def welcome(request):
    html = '<html><body>welcome to django</body></html>'
    return HttpResponse(html)

def hello(request):
    return HttpResponse('안뇽안뇽')

def template_test(request):
    # 기본 템플릿 폴더에서 읽어온다
    # 1.admin 앱에서 읽어온다
    # 2.각 앱의 폴더에 있는 template 폴더
    # 3.내가 설정한 폴더
    return render(request,'test.html')
    # test1.html 파일을 불러오게 된다. ㅋㅋㅋㅋ

# 함수형 뷰 만들기, 템플릿 만들기 , URL연결하기 , 브라우저 연습하기
# 이걸을 잘하면 굿이다


