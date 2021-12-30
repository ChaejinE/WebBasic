""" 
uuencode-encoding : 바이너리를 텍스트로 변환하기 위한 Encoding 방법

uuencode에서 uu는 Unix-to-Unix를 의미한다.
- 유닉스 시스템간 바이너리 데이터를 안전하게 전송하기 위해 만들어진 인코딩 방법이다.
- 하지만 단점이 보완된 base64, MIME 방식의 인코딩을 대부분 사용한다.
- uuㄹ 인코딩된 텍스트 파일은 begin ~ end 로 구성된다.
"""
import uu

# image to text
uu.encode("./image/test.jpg", "./result/result.txt")

# text to image
uu.decode("./result/result.txt", "./image/test1.jpg")