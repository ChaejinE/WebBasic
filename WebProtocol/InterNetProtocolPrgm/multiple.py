""" 
cgi : CGI 프로그램을 만들기 위한 도구를 제공하는 모듈이다.

CGI : 공통 게이트웨이 인터페이스, Common Gateway Interface의 약어로 웹서버와 
      외부 프로그램 사이에서 정보를 주고받는 방법이나 규약들을 말한다.
"""
#!/usr/bin/python3

import cgi
import cgitb

# 오류 발생 시 화면으로 바로보는 것이 편하다.
# 오류를 추적하기 가장 좋은 방법은 cgitb를 사용하는 것이다.
cgitb.enable()

# URL로 전달받은 두 개의 값 a, b를 얻으려면 cgi.FieldStorage Class가 필요하다.
# 이 Class를 사용하면 해당 값을 얻을 수 있다.
form = cgi.FieldStorage()

# getvalue(param) 을 호출하여 URL로 전달된 값을 얻을 수 있다.
a = form.getvalue('a')
b = form.getvalue('b')

# URL로 얻은 2개의 값은 숫자가 아닌 문자열이므로 숫자로 형변환을 해줘 곱해야한다.
result = int(a) * int(b)

# HTTP 규약에 따라 Content-type 항목과 빈줄을 포함해 출력해야한다.
# cgitb 기능을 활성화하면 plain이 아닌 html로 스크립트 최상단에 출력하면 좀 더 가독성있게 볼 수 있다.
print("Content-type: text/html")
print()
print("fResult:{result}")

# 위 프로그램은 아파치에서 /var/www/cgi-bin으로 설정했다면 
# /var/www/cgi-bin/multiple.py로 파일 경로가 셋팅 되어 있어야할 것이다.
