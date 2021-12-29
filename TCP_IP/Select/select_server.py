"""
기존 server를 구현할 때 문제점은 작업을 진행한 후 접속을 종료하면 소켓 서버가 종료되어 다른 클라이언트가 연결이 불가능하다.
또한, 소켓 서버가 동시에 여러 클라이언트들과 작업을 진행할 수 없다.
여러 클라이언트의 요청을 동시에 처리할 수 있도록 소켓 서버 프로그램을 수정해보자.

select 방식은 처음에 blocking 되어 있다가 특정 이벤트 발생 시 작동하는 방식이다. thread를 사용해도되지만 thread 사용 개수가 늘어날 수록
시스템에 무리를 주므로 효율적이지 않다. 그러므로 select 방식이 thread보다 효율적일 수 있다.
"""

import socket
import select
import random

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("server start")
    
    readsocks = [s]
    answers = {}
    
    while True:
        # select.select()는 readsocks에 포함된 소켓에서 이벤트가 발생하는지 감시하는 역할을 한다.
        # 감시하다가 readsocks에 속한 소켓에 이벤트가 발생하면 이후 문장들이 수행된다.
        # readables : 수신한 데이터를 지니고 있는 소켓을 의미한다.
        # writeables : blocking 되지 않고 데이터의 전송이 가능한 socket
        # exceptions : 예외 상황이 발생한 socket
        # 위 readables, writeables, exceptions 모두 리스트로 여러개의 소켓들로 구성된다.
        readables, writeables, exceptions = select.select(readsocks, [], [])
        for sock in readables:
            # 신규 클라이언트 접속
            if sock == s:
                newsock, addr = s.accept()
                answer = random.randint(1, 9)
                print(f"client : {addr}, answer : {answer}")
                readsocks.append(newsock)
                answers[newsock] = answer # client 별 정답 생성
            # 이미 접속한 클라이언트 요청
            else:
                conn = sock
                data = conn.recv(1024).decode('utf-8')
                print(f"data:{data}")
                
                try:
                    n = int(data)
                except ValueError:
                    conn.sendall(f"invalid input : {data}".encode("utf-8"))
                    continue
                
                answer = answers.get(conn)
                if n == 0:
                    conn.sendall(f"종료".encode('utf-8'))
                    conn.close()
                    readsocks.remove(conn)  # 클라이언트 접속 해제시 readsocks에서 제거
                if n > answer:
                    conn.sendall("너무 높아요".encode('utf-8'))
                elif n < answer:
                    conn.sendall("너무 낮아요".encode('utf-8'))
                else:
                    conn.sendall("정답".encode('utf-8'))
                    conn.close()
                    readsocks.remove(conn)  # 클라이언트 접속 해제시 readsocks에서 제거
