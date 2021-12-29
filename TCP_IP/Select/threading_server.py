import socket
import random
import threading

HOST = ''
PORT = 50007

def handle_client(conn, addr):
    with conn:
        answer = random.randint(1, 9)
        print(f"client : {addr}, answer : {answer}")
        
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(f("data:{data}"))
            
            try:
                n = int(data)
            except ValueError:
                conn.sendall(f"invalue value : {data}".encode('utf-8'))
                continue
            
            if n == 0:
                conn.sendall("end".encode('utf-8'))
                break
            
            if n > answer:
                conn.sendall("down".encode('utf-8'))
            elif n < answer:
                conn.sendall("up".encode('utf-8'))
            else:
                conn.sendall("정답".encode('utf-8'))
                break
            
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("server start")
    
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()