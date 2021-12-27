# Overview
- HTTP2.0은 HTTP1.1을 완전히 재작성한게 아닌 프로토콜의 성능에 초점을 맞춰 수정한 버전이다.
- End-User가 느끼는 Latency나 네트워크, 서버 릿스 사용량 등과 같은 성능 위주로 개선되었다.

# 특징
- Multiplexed Streams : connection 한 개로 동시에 여러 개의 메시지를 주고 받을 수 있으며 응답은 순서에 상관 없이 stream으로 주고받는다.
- Stream Prioritization : 리소스 간 의존관계에 따른 우선순위를 설정하여 리소스 로드 문제를 해결한다.
  - 문서 내 CSS 파일 1개, 이미지 파일 2개가 존재하고 이를 클라이언트가 요청하는 상황에서 이미지 파일보다 CSS 파일의 수신이 늦어진다면 렌더링에 문제가 생기게 되는데 이를 해결했다.
  - Server Push : 클라이언트가 요청하지 않은 리소스를 서버가 사전에 push를 통해 전송할 수 있다.
    - 푸시가 가능하면 클라이언트가 추후에 HTML 문서를 요청할 때 해당 문서 내의 리소스를 사전에 클라이언트에서 다운로드 할 수 있도록 하여 클라이언트의 요청을 최소화 할 수 있다.
- Header Compression
  - 헤더 정보를 HPACK 방식으로 압축한다.

![image](https://user-images.githubusercontent.com/69780812/147436489-8e59a4e4-f9b0-40ad-a309-1a6113825504.png)
- 위 처럼 클라이언트가 요청을 두번 보냈다고 가정해보자.
- HTTP 1.1의 경우 헤더 중복이 발생해도 중복 전송을 한다.
- 2.0의 경우 중복이 있는 경우 Static/Dynamic Header Table 개념을 이용해 중복을 검출해내고, 해당 테이블에서의 index값 + 중복되지 않은 Header 정보를 Huffman Encoding 방식으로 인코딩한 데이터를 전송한다.