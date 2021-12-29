import socket

HOST = "localhost"
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, port))
    
    while True:
        n = input("1-9")
        if not n.strip():
            print("invalid input")
            continue
        
        s.sendall(n.encode("utf-8"))
        # client는 socket 객체로 데이터를 주고 받는다.
        data = s.recv(1024).decode("utf-8")
        print(f"server response : {data}")
        if data == "good" or data == "end":
            break