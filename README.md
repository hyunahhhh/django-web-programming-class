# django-web-programming
 파이썬웹프로그래밍 예제코드

### 1. Web Framework
### 2. Django의 구조 : MVT
### 3. 홈페이지 구조
 - Main
 - Bookmark
 - 게시판
     . 게시글 읽기, 쓰기, 삭제, 수정
     . 태그
     . 댓글
     . 아카이브
 - 사진첩


### 4. Django 설치
 - venv
 - django

>   <u>(참고) Anaconda 사용자, SSL 에러 발생</u>  
>     - [해결방법]  
>       Anaconda3\Library\bin 안에 있는 파일 4개를   
>       (libcrypto-1_1-x64.* libssl-1_1-x64.*)   
>       Anaconda3\DLLs 아래로 복사  


### 5. 프로젝트 뼈대 만들기
 - django-admin startproject mysite     
 - python mange.py migrate           

>   (참고) Anaconda 사용자, sqlite3 에러 발생  
>     - [해결방법]  
>        https://www.sqlite.org/download.html 에서 파일 다운로드 >   
>        압축 해제 > sqlite3.def, sqlite3.dll 파일 >  
>        C:\Windows\System32에 복사  

 - python manage.py createsuperuser   
 - python manage.py startapp bookmark  
 - python manage.py runserver         // Run > Edit Configurations   
 - 127.0.0.1/8000  

### 6. 프로젝트 개발 순서

#### 1) 설계

-  화면설계 : 화면, view, url, html
-  데이터베이스 설계

#### 2) 모델(models.py, admin.py)

-  데이터베이스 설계한 필드를 파이썬 코드로 정의 후, 아래 두 명령어를 사용해서 데이터베이스에 테이블 생성 
-  python mange.py makemigrations
-  python mange.py migrate 

#### 3)  URL(urls.py), 뷰(views.py), 템플릿(.html) 

#####  urls.py

- 어플리케이션 별로 url을 관리하는 것이 추후 유지보수 시 편리함

- url 경로, 처리할 view를 명시적으로 지정

- name 속성을 설정할 경우, html 파일에서 참고하여 호출할 수 있음

- base.html

  ```
  <a class="dropdown-item" href="{% url 'board:index' %}">Posts</a>
  <a class="dropdown-item" href="{% url 'board:search' %}">Search</a>
  ```

- board/urls.py

  ```
   path('', views.PostListView.as_view(), name='index'),
   path('search/', views.SearchFormView.as_view(), name='search')
  ```



##### views.py

- urls.py에서 정의한 view의 실체를 구현
- 보통 장고에서 기본으로 제공하는 Generic View(ListView, DetailView 등)를 상속받아 사용
- 기본적으로 부모 클래스에서 정의한 "html 파일명"과 "object 형태"가 있어 명시적으로 속성값을 지정하지 않아도 됨
- model은 어떤 테이블을 참고해야하는지 정의 필요함



##### 템플릿(*.html)

######  템플릿의 상속

-  BootStrap을 활용한 화면 꾸미기

  -  부트스트랩 공식사이트: https://getbootstrap.com/
  -  부트스트랩 템플릿사이트: https://startbootstrap.com/

- 화면 구성시 참고하는 리소스 파일(css, 이미지 파일 등)은 static으로 지정

  - https://docs.djangoproject.com/ko/3.0/intro/tutorial06/

- 전체 화면에서 공통으로 사용하는 부분은 base.html에 구현하고, block을 지정한 부분은 상속받은 html 페이지에서 구현

- ```
  {% extends 'base.html' %}
  
  {% load static %}
  
  {% block title %}home.html {% endblock %}
  
  {% block header %}{% endblock %}
  
  {% block content %}{% endblock %}
  
  {% block footer %}{% endblock %}
  
  {% block extra-script %}{% endblock %}
  ```



#### 7. 인증기능(로그인/로그아웃)

- 로그인 이전 상태

  - 로그인(login.html) 
  - <u>회원가입(register.html) → 회원가입 완료(register_done.html)</u>

- 로그인 상태

  - 로그아웃(logged_out.html) 
  - 비밀번호 변경(password_change_form.html)  →  비밀번호 변경 완료(password_change_done.html)

  (참고) https://github.com/django/django/blob/master/django/contrib/auth/urls.py

- form  꾸미기:  widget-tweaks 앱
  - https://pypi.org/project/django-widget-tweaks/
  - https://github.com/jazzband/django-widget-tweaks
- (참고) form 
  -  https://www.w3schools.com/html/html_forms.asp
  - get/post : https://www.guru99.com/php-forms-handling.html#7



#### 8. 편집하기(입력/수정/삭제) - Bookmark

1. ##### 설계

- 화면 설계

  bookmark_list.html : '새로 만들기' 버튼 추가  →  [새로만들기 Form]

  bookmark_detail.html: '수정/삭제' 버튼 추가  → [수정하기 Form / 삭제 Form]

- DB 설계

  - owner 필드 추가: ForeignKey(User)

- 새로 만들기: /bookmark/add/ → BookmarkCreateView → bookmark_form.html
- 수정 하기 :   /bookmark/1/update/ → BookmarkUpdateView → bookmark_form.html
- 삭제하기  :   /bookmark/1/delete/ → BookmarkDeleteView → bookmark_confirm_delete.html



2. ##### models.py

   ```
   #추가
   from django.contrib.auth.models import User
   
   #사용자를 foreignkey로 할당하기 위한 field 생성
   owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
   
   ```

   makemigrations, migrate



3. ##### urls.py

   - import 구문

   ```
   # from bookmark.views import BookmarkLV, BookmarkDV
   from bookmark import views
   ```

   - 본문

   ```
   # 리스트: http://127.0.0.1:8000/bookmark/
   # 수정해보기
   path('', BookmarkLV.as_view(), name='index'),
   
   # 상세페이지: http://127.0.0.1:8000/bookmark/1/
   # 수정해보기
   path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
   
   # 생성: http://127.0.0.1:8000/bookmark/add/
   path('add/', views.BookmarkCreateView.as_view(), name="add",),
   
   # 수정: http://127.0.0.1:8000/bookmark/1/update/
   path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update",),
   
   # 삭제: http://127.0.0.1:8000/bookmark/1/delete/
   path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete",),
   ```

   

4. ##### views.py

   - <u>mysite/views.py</u>		

     ```
     from django.contrib.auth.mixins import AccessMixin
     
     ## 중간 생략
     
     class OwnerOnlyMixin(AccessMixin):
         raise_exception = True
         permission_denied_message = "Owner only can update/delete the object"
     
         def get(self, request, *args, **kwargs):
             self.object = self.get_object()
             if self.request.user != self.object.owner:
                 self.handle_no_permission()
             return super().get(request, *args, **kwargs)
     ```

     blog/views.py

   - import 구문

   ```
   from django.views.generic import CreateView, UpdateView, DeleteView
   from django.contrib.auth.mixins import LoginRequiredMixin
   from django.urls import reverse_lazy
   from mysite.views import OwnerOnlyMixin		
   ```

   - 뷰 구문 추가

   <u>bookmark/views.py</u>

   ```
   class BookmarkCreateView(LoginRequiredMixin, CreateView): 
       model = Bookmark 
       fields = ['title', 'url'] 
       success_url = reverse_lazy('bookmark:index') 
   
       def form_valid(self, form): 
           form.instance.owner = self.request.user 
           return super().form_valid(form)
   
   
   class BookmarkUpdateView(OwnerOnlyMixin, UpdateView): 
       model = Bookmark 
       fields = ['title', 'url'] 
       success_url = reverse_lazy('bookmark:index') 
   
   
   class BookmarkDeleteView(OwnerOnlyMixin, DeleteView): 
       model = Bookmark 
       success_url = reverse_lazy('bookmark:index')
   ```



​		