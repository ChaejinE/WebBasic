""" 
quopri : quoted-printable Encoding/Decoding 시 사용하는 모듈이다.

quoted-printable
- 위 Encoding 방식은 인코딩된 메시지를 디코딩하지 않더랃 ASCII 문자들이 그대로 보일 수 있도록 하는 방식이다.
- 즉, 영문자와 숫자등의 ASCII 7bit 문자들은 그대로 두고 8bit 문자만 인코딩하는 방식이다.
"""
import quopri

# decodestring()은 바이트 문자열을 return한다. 그래서 utf-8로 디코딩
print(quopri.decodestring('Python Library =EA=B3=B5=EB=B6=80').decode('utf-8'))

# 아래 문자열은 quopri 모듈을 이용해 quoted-printable 방식으로 인코딩하는 방법이다.
print(quopri.encodestring("Python Library 공부".encode('utf-8')))