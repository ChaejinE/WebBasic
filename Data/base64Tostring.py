"""
base64 : 바이너리 데이터를 문자열로 인코딩할 때 사용하는 모듈이다.
인코딩된 문자열은 64개의 ASCII 문자들로 구성된다. (64진법 사용)

base64는 바이너리 데이터를 이메일에 첨부할 수 있는 방법을 고안된 인코딩 방법이다.

A가 B에게 이미지 파일을 전송하고 싶어한다고 해보자.
A는 이미지 파일을 base64 형식으로 인코딩된 문자열로 바꿔주는 img_to_string 함수가 필요하다.
그리고 B는 데이터를 수신받아 다시 base64로 인코딩된 문자열을 이미지로 바꿔주는 string_to_img 함수가 필요하다.
"""
import base64

def img_to_string(filename):
    """
    file name을 입력으로 받아 base64로 인코딩한 문자열을 Return
    """
    with open(filename, "rb") as f:
        return base64.b64encode(f.read())
    
def string_to_img(s, filename):
    """
    base64로 인코딩된 문자열(s)와 filename을 입력으로 받아 문자열을 파일로 저장한다.
    """
    with open(filename, "wb") as f:
        f.write(base64.b64decode(s))
        
img_string = img_to_string("./image/test.jpg")
string_to_img(img_string, "./result/result.jpg")