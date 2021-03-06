# Overview
- HTTP 1.1, HTTP 2.0의 큰 차이는 속도다.
- 2.0은 header를 압축해서 보내기도 하고 한번의 연결로 동시에 에러 메시지를 주고 받을 수 있다.

# HTTP1.1 문제점 (특징)
- Connection 한개 당 하나의 요청을 처리하도록 설계되었다.
  - 동시에 리소스를 주고 받는 것이 불가능하다.
  - 요청과 응답이 순차적으로 이뤄진다.
  - HTTP 문서 내에 포함된 다수의 리소스를 처리하려면 요청할 리소스의 개수에 비례해 Latency(대기시간)이 길어진다.
    - 리소스 : Image, css, script 등
- HOL(Head  Of Line) Blocking이 발생할 수 있다.
  - 이는 네트워크에서 같은 queue에 있는 패킷이 첫 번째 패킷에 의해 지연될 때 발생하는 성능 저하 현상을 말한다.
- RTT(Round Trip Time) 증가
  - Connection 하나에 요청 한개를 처리하는 특성 때문에 매번 요청 별로 Connection을 만들게 되고 TCP 상에서 동작하는 HTTP 특성상 3-way handshake가 반복적으로 일어난다. 불필요한 RTT 증가와 네트워크 지연을 초래해 성능을 지연시킨다.
- 무거운 Header구조
  - 매 요청마다 중복된 헤더값을 전송하게 되어 서버 도메인에 관련된 쿠기 정보도 헤더와 함께 포함되어 전송된다.
  - 이러한 반복적인 헤더 전송, 쿠키 정보로 인해 헤더 크기가 증가할 수 있다.

# 개선 방법
- Image Spriting : 웹 페이지를 구성하는 다양한 아이콘 이미지 파일의 요청 횟수를 줄이기 위해 아이콘을 하나의 큰 이미지로 만든 다음 CSS에서 해당 이미지의 좌표 값을 지정하여 표시하는 방법이다.
- Domain Sarding : 브라우저들이 HTTP1.1의 단점을 극복하기 우해 여러 개의 Connection을 생성해서 병렬로 요청을 보내기도 한다. 하지만 브라우저 별로 도메인 당 Connection 개수 제한이 존재해 근본적인 해결을 어렵다.
- Minified CSS/Javascript
  - HTTP를 통해 전송되는 데이터의 용량을 줄이기 위해 CSS, Javascript를 축소한다.
- Loader Faster
  - head 태그에 자바 스크립트 삽입하고, async나 defer 옵션을 사용해 브라우저의 파싱을 block하지 않고 로드한다.
- Data URI Scheme
  - HTML문서 내 이미지 리소스를 Base64로 인코딩된 이미지 데이터로 직접 기술하는 방법으로 서버로의 요청을 줄인다.
- 구글의 SPDY
  - 위에서 언급된 노력들ㄹ는 근본적 단점을 해결할 수 없었다. 그래서 구글은 더 빠른 웹을 실행하기 위해 Throughput 관점이 아닌 Latency 관점에서 HTTP를 고속화한 SPDY라 불리는 새로운 프로토콜을 구현했다.
  - 다만 HTTP를 대체하는 규격은 아니었고 HTTP를 통한 전송을 재정의하는 형태로 구현되었다. 이는 HTTP2.0의 참고 규격이 된다.
