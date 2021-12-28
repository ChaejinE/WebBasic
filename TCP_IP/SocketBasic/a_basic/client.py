import socket

host = "127.0.0.1"
port = 9999

# 통신할 소켓 오픈
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server accept()에 연결 요청
# server와 같은 host, port 여야한다.
client_socket.connect((host, port))

while True:
    msg = input("msg:")
    # server로 msg 전송
    client_socket.sendall(msg.encode())
    
    # server로 부터 1024 크기만큼 수신
    data = client_socket.recv(1024)
    print("Received", data.decode())
    
    if msg == '/stop':
        break
    
client_socket.close()