# MIME(Multi-purpose INternet Mail Extensions)
- SMTP로 전송 시 이메일에 텍스트 밖에 포함하지 못하는 단점을 보완했다.
- 메시지 안에 텍스트 이외 데이터를 전송할 수 있도록 하는 프로토콜

# 특징
- 1. 바이너리 파일을 출력 가능한 문자열 형태로 인코딩하고, 수신하는 부분에서 디코딩한다.
- 2. Base64ㄹ 인코딩하기는 하나 다른 형태의 인코딩도 사용할 수 있다.
  - 인코딩 방식은 메시지의 헤더안에서 정의한다.

```
MIME-Version: 1.0
Content-Type: Multipart/Mixed; Boundary=Mime.separator
```
- 위의 MIME 버전은 1.0
- 각 메시지 앞에 Mime_separator가 나타남을 명시한다.
  - 텍스트만 보내는 경우에는 Content-Type이 text/plain이 된다.
- 결론적으로 MIME는 이메일 메시지 안의 header에 추가 정보를 포함해 비 텍스트형 데이터가 전송될 수 있도록하는 프로토콜이다.