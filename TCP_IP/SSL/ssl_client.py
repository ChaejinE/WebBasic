import socket
import ssl

HOST = 'localhost'
PORT = 50007

# socket 생성 전 client를 위한 context 객체를 먼저 만든다.
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# Client를 위한 인증서를 load 한다.
context.load_verify_locations('CA.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # client socket은 context를 통해 아래 처럼 감싸줘야한다.
    # 사용되는 server host name은 server.csr 파일 생성할 때 등록한 host명(common name)과 일치 해야한다.
    with context.wrap_socket(sock, server_hostname='cjlotto') as s:
        s.connect((HOST, PORT))

        while True:
            n = input("1-9 사이의 숫자를 입력하세요(0은 게임포기):")
            if not n.strip():
                print("입력값이 잘못되었습니다.")
                continue
            s.sendall(n.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            print(f'서버응답:{data}')
            if data == "정답" or data == "종료":
                break