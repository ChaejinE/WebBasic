# 인증서 생성
```shell
openssl
```
- linux 환경에서 openssl을 사용하여 인증서를 생성한다.

```
OpenSSL> genrsa -out CA.key 2048
```
- 위 명령어로 CA.key 파일을 생성한다.

```
OpenSSL> req -x509 -new -nodes -key CA.key -days 365 -out CA.pem
```
- 위 명령으로 CA.pem 파일을 생성한다.
- 국가 코드만 KR로 바꾸고 모든 항목은 비워서 생성했다.
- CA.pem은 CA.key가 필요하며 유효기간은 365일이다.

```
OpenSSL> genrsa -out server.key 2048
```
- 위 명령으로 server.key 파일을 생성한다.

```
OpenSSL> quit
openssl
```
- server.key 생성 후 server.csr 파일 생성하기 전 반드시 openssl 프롬프트를 종료하고 다시 시작해야한다.
- openssl을 재식하지 않고 생성하면 'problem creating object tsa_policy1=1.2.3.4.1'와 같은 오류를 만나게 된다.

```
req -new -key server.key -out server.csr
```
- Common Name 항목에서는 'cjlotto'를 입력했다.

```
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:KR
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:cjlotto
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
OpenSSL> x509 -req -in server.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out server.crt
Signature ok
subject=C = KR, ST = Some-State, O = Internet Widgits Pty Ltd, CN = cjlotto
Getting CA Private Key
```

```
x509 -req -in server.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out server.crt
```
- 마지막으로 위 명령어로 server.crt 파일을 생성한다.