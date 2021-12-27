import socket

# server ip (local host)
host = '127.0.0.1'

# server port
port = 9999

# socket server open
# AF_INET(주소체계 IPv4, SOCK_STREAM:tcp)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# port 여러번 bind 시 발생하는 에러 방지 (없어도된다.)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind : open 할 socket에 host, port 전달
server_socket.bind((host, port))

# client가 accept 할수 있게된다. - 접속 허용
server_socket.listen()

print("start server")

# accept : client 접속 wait. 요청 시 처리
# client와 1:1 통신할 소켓, 연결된 상대방 주소 반환
client_socket, addr = server_socket.accept()

print("Connected by", addr)

while True:
    # recv(size), 소켓에서 1024만큼 메시지를 읽는다.
    data = client_socket.recv(1024)
    
    # Encoding message decoding
    msg = data.decode()
    print("Received from", addr, msg)
    
    # client로부터 받은 메시지 다시 전송
    client_socket.sendall(data)
    
    if msg == '/stop':
        break

# socket 종료
client_socket.close()
server_socket.close()
    