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

  (참고) Anaconda 사용자, SSL 에러 발생  
    - [해결방법]  
      Anaconda3\Library\bin 안에 있는 파일 4개를   
      (libcrypto-1_1-x64.* libssl-1_1-x64.*)   
      Anaconda3\DLLs 아래로 복사  


### 5. 프로젝트 뼈대 만들기
 - django-admin startproject mysite     
 - python mange.py migrate           

  (참고) Anaconda 사용자, sqlite3 에러 발생  
    - [해결방법]  
       https://www.sqlite.org/download.html 에서 파일 다운로드 >   
       압축 해제 > sqlite3.def, sqlite3.dll 파일 >  
       C:\Windows\System32에 복사  

 - python manage.py createsuperuser   
 - python manage.py startapp bookmark  
 - python manage.py runserver         // Run > Edit Configurations   
 - 127.0.0.1/8000  
