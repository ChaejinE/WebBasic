"""
selectors는 selector 모듈을 확장한 모듈이다.
select 대신 사용하도록 권장되는 모듈이다.
"""
import socket
import selectors
import random

HOST = ''
PORT = 50008

# selectors에는 EpollSelector, KqueueSelector 등 여러 Selector가 있다.
# DefaultSelector는 해당 시스템에서 사용할 수 있는 최적의 Selector를 Return 해준다.
# Ex) BSD -> KqueueSelector()
sel = selectors.DefaultSelector()
answers = {}

# Selectors 모듈은 DefaultSelector로 생성한 객체에 Event(실행할 Function)을 등록해야 하는 구조다.
# 그러므로 Client 접속을 처리하는 함수 accept_client, client가 작업하는 game_client를 작성한다.
def accept_client(sock):
    """
    server socket에 client가 connect되면 호출된다.
    """
    conn, addr = sock.accept()
    answer = random.randint(1, 9)
    answers[conn] = answer
    
    # client socket 등록
    # client socket에 데이터가 수신되면 game_client function이 실행되도록 설정한 것이다.
    # Event에는 EVENT_READ(읽기), EVENT_WRITE(쓰기)가 있다.
    sel.register(conn, selectors.EVENT_READ, game_client)
    print(f"client : {addr}, answer : {answer}")
    
def game_client(conn):
    """
    client socket에서 data 수신 시 호출된다.
    """
    data = conn.recv(1024).decode('utf-8')
    print(f"data:{data}")
    
    try :
        n = int(data)
        answer = answers.get(conn)
        if n == 0: 
            conn.sendall(f"종료".encode('utf-8'))
            sel.unregister(conn)
            conn.close()
        elif n > answer:
            conn.sendall("너무 높아요".encode('utf-8'))
        elif n < answer:
            conn.sendall("너무 낮아요".encode('utf-8'))
        else:
            conn.sendall("정답".encode('utf-8'))
            sel.unregister(conn)
            conn.close()
    except ValueError:
        conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("server start")
    # sever socket에 client 접속 시 accept_client 함수 실행하도록 설정
    sel.register(s, selectors.EVENT_READ, accept_client) # server socket 등록
    
    while True:
        # client의 접속 or 접속된 client의 데이터 요청 감시
        # 등록한 Server(socket)의 event 감시
        events = sel.select()
        
        # mask : EVENT_READ or EVENT_WRITE를 의미하는 숫자값이다.
        for key, mask in events:
            # 실행할 function
            # sel.register로 등록한 Callback function
            callback = key.data
            
            # 이벤트가 발생한 소켓을 인수로 실행할 function을 실행한다.
            # key.fileobj : 이벤트가 발생한 socket
            callback(key.fileobj)