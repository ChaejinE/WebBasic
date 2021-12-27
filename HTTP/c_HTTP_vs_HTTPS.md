# Overview
- HTTP, HTTPS 둘다 웹 서버가 브라우저로부터 요청을 받아 응답할 때 사용되는 프로토콜이다.
- HTTP : www에서 html 문서를 송수신 하기 위한 표준 프로토콜
- HTTPS : HTTP에 ㅂ안 모듈을 결합시킨 프로토콜

# 1. HTTP
- 인터넷에서 하이퍼텍스트를 교환하기 위한 통신규약
  - 80번 포트 사용
  - 따라서 HTTP 서버가 80번 포트에서 요청을 기다리고 있으며 클라이언트는 80번 포트로 요청을 보내게된다.

![image](https://user-images.githubusercontent.com/69780812/147436695-a68d2e0e-3719-4446-8cf4-907feecb436f.png)
- 어플리케이션 레벨의 프로토콜로 TCP/IP 위에서 작동한다.
- 상태를 가지고 있지 않은 statless 프로토콜이다.
- method, path, version, headers, body 등으로 구성된다.
- 암호화 되지 않은 평문 데이터를 전송하는 프로토콜이다.
  - HTTPㄹ 보안이 중요한 데이터를 주고 받으면 제 3자가 정보를 조회할 수 있다. (보안 취약)

# 2. HTTPS(Hyper Text Transfer Protocol Secure)
![image](https://user-images.githubusercontent.com/69780812/147436820-0112f199-0c2e-4d00-aaeb-20f0523c9eb5.png)
- HTTP over Secure Socket Layer 등으로 불린다.
- HTTP에 암호화가 추가된 프로토콜이다.
- 443번 포트를 사용한다.
- 네트워크 상 중간에 제 3자가 정보를 볼 수 없도록 공개키 암호화를 지원하고 있다.
- 암호화/복호화 과정이 필요해 HTTP 보다 속도가 느리다. (체감하기는 어렵다고한다.)
- 인증서 발급하고 유지하기 위한 **추가비용이 발생**한다.

# Conclusion
- 개인 정보와 같은 민감한 데이터를 주고 받는 다면 HTTPS를 사용해야하지만 단순 정보 조회 등만 처리한다면 HTTP를 이용하면 된다.