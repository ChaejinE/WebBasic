# HTTP (Hyper Text Transfer Protocol)
- 브라우저가 웹서버와 통신하기 위해 사용하는 주요 프로토콜이다.
  - 인터넷에서 데이터를 주고 받을 수 있는 통신규약으로 생각하면 된다.

# 특징
- 암호화 되지 않은 평문 데이터를 전송하는 프로토콜
  - 보안이 중요한 데이터를 주고 받으면 제 3자가 정보를 조회할 수 있다.
  - 즉, 보안이 취약하다.
- 상태가 없는 프로토콜 (stateless)
  - 데이터를 주고 받기 위한 각각의 데이터 요청이 서로 독립적으로 관리된다.
  - 이전 데이터 요청과 다음 데이터 요청이 서로 관련이 없다는 뜻이다.
  - 이러한 특징으로 서버는 세션과 같은 별도의 추가 정보를 관리하지 않아도 다수의 요청 처리 및 서버의 부하를 줄일 수 있는 성능 상의 이점이 있다.
- HTTP는 일반적으로 TCP/IP 통신 위에서 동작하며 기본 포트는 80이다.
- start line, headers, body 등으로 구성된다.
  - start line : method, path, version

# 통신 방식
![image](https://user-images.githubusercontent.com/69780812/147432376-3483cb58-1a75-4cba-ae20-aad0651680c6.png)
- Client가 요청을 보내고 Server가 응답을 받는다.
  - Client는 웹 관점에서는 브라우저를 의미한다.
  - Server는 웹 관점에서 데이터를 보내주는 원격지의 컴퓨터를 의미한다.
  - Ex) URL에 사이트 주소를 입력하고 확인을 누르면 브라우저에서 GET 요청으로 서버에 페이지를 요청한다. GET 요청을 받은 Server에서는 헤더와 요청한 문서를 클라이언트로 보낸다.

## 1 HTTP Request
- start line, headers, body 3가지로 구성된다.

### 1.1 start line
```
GET /search HTTP/1.1
```
- HTTP Method : 해당 request가 의도한 action을 정의하는 부분
- Request target : 해당 request가 전송되는 목표 URI
- HTTP version : 사용되는 프로토콜 버전 (1.0, 1.1, 2.0 등)

### 1.2 Headers
- 해당 request에 대한 추가 정보를 담고 있는 부분
- key : value로 되어있다.
- Headersㄷ 크게 3부분으로 나뉘지만 매우 자세한 부분으로 3부분으로 나뉜다고만 알고 있자.
  - general headers
  - request headers
  - entity hedaers

```
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/json
Content-Length: 257
Host: google.com
User-Agent: HTTPie/0.9.3
```
- 자주 사용되는 header 정보
  - Host : 요청이 전송되는 target의 url
  - User-Agent : 요청을 보내는 클라이언트에 대한 정보
  - Accept : 해당 요청이 받을 수 있는 Reponse type
  - Connection: 해당 요청이 끝난 후 클라이언트와 서버가 계속해서 네트워크 커넥션을 유지할 것인지 아니면 끊을 것인지에 대한 지시 부분
  - Content-Length: 메세지 body 길이

### 1.3 Body
```
{
    "imp_uid": "imp_1234567890",
    "merchant_uid": "order_id_8237352"
    "status": "paid"
}
```
- 해당 Request의 실제 메시지/내용
- Body가 없는 request도 많다. (GET request 대부분)

## 2. HTTP Response
- Request와 마찬가지로 3부분으로 구성되어있다.
- Status line, Headers, Body

### 2.1 Status line
- Response 상태를 간략하게 나타내주는 부분
```
HTTP/1.1 404 Not Found
```
- HTTP version
- Status code : 응답 상태를 나타내는 숫자값
- Status text : 응답 상태를 간략하게 설명해주는 상태 문자

### 2.2 Headers
- Response의 headers와 동일
  - 다만, User-Agent 대신 Server header가 사용되는 등 response에서만 사용되는 header가 있다.

### 2.3 Body
- Reponse body와 일반적으로 동일
- Request와 마찬가지로 모든 response가 body가 있지는 않다.
- 데이터를 전송할 필요가 없는 경우 body가 비어있게 된다.

## 3. 자주 쓰이는 HTTP Method
- 요청하는 데이터에 특정 동작을 수행하게 하고 싶을 때 사용하는 메서드다.
  - HTTP Verbs라고도 불린다.
- GET : 존재하는 자원에 대한 요청(조회)
- POST : 새로운 자원 생성
- PUT : 존재하는 자원에 대한 변경 (전체)
- PATCH : 존재하는 자원에 대한 변경 (일부)
- DELETE : 존재하는 자원에 대한 삭제
- HEAD : 서버 헤더 정보를 획득
  - GET과 비슷하지만 Response Body를 반환하지 않는다.
- OPTIONS : 서버 옵션들을 확인하기 위한 요청 CORS에 사용

## 4. 자주 쓰이는 HTTP 상태 코드
- URL과 요청 메서드가 클라이언트에서 설정해야할 정보라면 HTTP 상태 코드는 서버에서 설정해주는 응답 정보이다.
  - 200번대 부터 500번대까지 다양하게 있지만 주요 상태 코드만 몇개 살펴볼 것

### 4.1 2xx - 성공
- 200번대 상태 코드는 대부분 성공을 의미한다.
- 200 : GET 요청에 대한 성공
- 204 : No Content. 성공했으나 응답 본문에 데이터 없음
- 205 : Reset Content. 성공했으나 클라이언트 화면을 새로 고침하도록 권고
- 206 : Partial Content. 썽공했으나 일부 범위의 데이터만 반환

### 4.2 3xx - redirection
- 300번대는 대부분 클라이언트가 이전 주소로 데이터를 요청하여 서버에서 새 URL로 리다이렉트를 유도하는 경우다.
- 301 : Moved Permanently. 요청한 자원이 새 URL에 존재
- 303 : See Other. 요청한 자원이 임시주소에 존재
- 304 : Not Modified. 요청한 자원이 변경되지 않았으므로 클라이언트에서 캐싱된 자원을 사용하도록 권고
  - Etag와 같은 정보를 통해 변경여부 확인

### 4.3 4xx - 클라이언트 에러
- 400번대 상태 코드는 대부분 클라이언트의 코드가 잘못된 경우이다.
- 400 : Bad Request. 잘못된 요청
- 401 : Unauthorized. 권한 없이 요청, Authorization 헤더가 잘못된 경우
- 403 : Forbidden. 서버에서 해당 자원에 대해 접근 금지
- 405 : Method Not Allowed, 허용되지 않은 요청 메서드
- 409 : Conflict. 최신 자원이 아닌데 업데이트하는 경우
  - 파일 업로드 시 버전 충돌

### 4.4 5xx - 서버 에러
- 500 번대 상태 코드는 서버 쪽에서 오류가난 경우이다.
- 501 : Not Implemented. 요청한 동작에 대해 서버가 수행할 수 없는 경우
- 503 : Service Unavailable. 서버가 과부하 또는 유지 보수로 내려간 경우

## 5. 브라우저에서 캐싱하기
- 웹페이지 성능을 최적화하려면 캐시를 이용한다.
- 용량이 큰 이미지가 많은 사이트를 반복 접속하는 경우 다운로드 시간과 HTTP GET 요청수를 줄이기 위해 해당 이미지를 사용자의 디스크에 저장하고 캐시로 사용한다.
- 브라우저는 캐시가 최신 버전인지 이전 버전인지 어떻게 확인 하는가 ?
  - 캐시는 사용하기 전에 서버에 HEAD 요청을 날려 Last-Modified Data를 비교해 최신임을 확인한다.
- 주의할 것은 모든 파일에 대해 캐시를 만들지 아니면 HEAD 요청을 만들어 날리는 값들을 고려했을 때 캐시로 만들지 않는 것이 효율적인지 고민해야한다. (캐시하려는 파일의 크기가 매우 작을 수 있기 때문)