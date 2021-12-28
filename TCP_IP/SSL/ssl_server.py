"""
ssl 모듈 : socket 모듈로 작성된 서버/클라이언트에 공개키 암호화 방식을 적용할 때 사용하는 모듈

SSL(Secure Socket Layer)는 네트워크로 연결된 컴퓨터간 인증되고 암호화된 링크를 설정하기 위한 프로토콜이다.

공개키 암호화 방식이란, 공개키와 비밀키를 사용해 암호화하는 방식이다.
비밀키로 암호화된 데이터는 공개키로만 복호화되고, 공개키로 암호화된 데이터는 비밀키로만 복호화되는 방식이다.
- 공개키 : 누구에게나 공개되는 키
공개키로 암호화된 데이터는 오직 비밀 키를 가지고 있는 서버에서만 복호화가 가능하므로 클라이언트가 서버로 안전하게 메시지를 발송할 수 있게 해주는 암호화 방법이다.

ssl 모듈 적용을 위해 다음과 같은 파일들이 필요하다.
1. CA.key : 공개키
2. CA.pem : 공개키를 바탕으로 만들어진 인증서 (Client에 제공해야하는 인증서)
3. server.key - 비밀키 (서버에만 존재)
4. server.crt - 서버 인증서 (서버에만 존재해야하는 인증서)
"""

import socket
import ssl
import random

host = ''
port = 50007

# socket 서버에 ssl 적용하기 위해서는 context 객체를 먼저 생성해야한다.
# server socket 이므로 PROTOCOL_TSL_SERVER를 전달해주면된다.
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# 생성한 서버 인증서 파일 및 서버 키 파일을 로드한다.
context.load_cert_chain('server.crt', 'server.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    print('서버가 시작되었습니다.')

    # 생성한 소켓은 context를 사용해 아래처럼 감싸줘야한다.
    with context.wrap_socket(sock, server_side=True) as s:
        conn, addr = s.accept()
        with conn:
            answer = random.randint(1, 9)
            print(f'클라이언트가 접속했습니다:{addr}, 정답은 {answer} 입니다.')
            while True:
                data = conn.recv(1024).decode('utf-8')
                print(f'데이터:{data}')

                try:
                    n = int(data)
                except ValueError:
                    conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                    continue

                if n == 0:
                    conn.sendall(f"종료".encode('utf-8'))
                    break
                if n > answer:
                    conn.sendall("너무 높아요".encode('utf-8'))
                elif n < answer:
                    conn.sendall("너무 낮아요".encode('utf-8'))
                else:
                    conn.sendall("정답".encode('utf-8'))
                    break