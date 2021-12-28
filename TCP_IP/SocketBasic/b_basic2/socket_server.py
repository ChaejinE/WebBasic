from os import RTLD_NOLOAD
import socket
import random

host = '' # host에 빈문자열이면 외부 접속이 허용된다.
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print("server start")
    conn, addr = s.accept()
    
    with conn:
        answer = random.randint(1, 9)
        print(f"client : {addr}, answer is {answer}")
        while True:
            # server는 conn으로 데이터를 주고받는다.
            data = conn.recv(1024).decode("utf-8")
            print(f"data:{data}")
            
            try:
                n = int(data)
            except ValueError:
                conn.sendall(f"invalid input : {data}".encode("utf-8"))
                continue
            
            if n == 0:
                conn.sendall(f"end".encode("utf-8"))
                break
            if n > answer:
                conn.sendall("down".encode("utf-8"))
            elif n < answer:
                conn.sendall("up".encode("utf-8"))
            else:
                conn.sendall("good".encode("utf-8"))
                break
            