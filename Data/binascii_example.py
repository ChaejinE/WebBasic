""" 
binascii : 문자열과 16진수간 변환을 위해 사용하는 모듈
"""
import binascii

some_encode = '507974686f6e204c696272617279'
some_str = b'507974686f6e204c696272617279'

# binascii.unhexlify() 사용 시 16진수 문자열로 변환된 원래 문자열 값을 쉽게 얻을 수 있다.
# 입력은 바이트 문자열임에 주의하자.
print(binascii.unhexlify(some_str))

# string -> 16진수 : binascii.hexlify()를 사용한다.
print(binascii.hexlify(b"Python Library"))
# 한국어 사용 시 utf-8로 인코딩해줘야한다.
print(binascii.hexlify("파이썬 라이브러리".encode('utf-8')))

# 또는 바이트 문자열의 hex() 함수 사용
print(b"Python Library".hex())



# bytes 자료형은 사용해도 된다.
print(bytes.fromhex(some_encode))
