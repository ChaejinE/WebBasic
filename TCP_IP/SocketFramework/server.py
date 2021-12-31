""" 
socketserver 모듈은
- 여러 형태의 소켓 서버를 쉽게 구현하기 위해 사용하는 모듈이다.
- 저수준 모듈인 socket을 사용할 필요없이 이 모듈만 사용하면된다.
"""

import socketserver
import random

class MyTCPHandler(socketserver.BaseRequestHandler):
    """ 
    socket 모듈 사용 시 필요했던 bind, listen, accept 와 같은 일을
    TCPServer가 모두 대신 처리한다.
    Client 요청은 MyTCPHandler를 구현해 처리한다.
    BaseRequestHandler를 상속해 handle method를 구현해야한다.
    handle 메서드는 클라이언트 접속 시 실행되는 함수다.
    self.request는 접속한 클라이언트 소켓을 의미한다.
    """
    def handle(self):
        answer = random.randint(1, 9)
        print(f"client : {self.client_address[0]} \
                answer = {answer}")
        
        while True:
            data = self.request.recv(1024).decode('utf-8')
            print(f"data:{data}")
            
            try:
                n = int(data)
            except ValueError:
                self.request.sendall(f"")
                continue
            
            if n == 0:
                self.request.sendall(f"종료".encode('utf-8'))
                break
            if n > answer:
                self.request.sendall("down".encode('utf-8'))
            elif n < answer:
                self.request.sendall("up".encode('utf-8'))
            else:
                self.request.sendall("ok")
                break

            
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ 
    ThreadMixIn 클래스를 이용해 여러개 클라이언트 요청 처리 할 경우 스레드 처리를 용이하게 할 수 있다.
    ThreadingMixln과 TCPServer를 함께 상속해 만든 ThreadedTCPServer 클래스이며
    TCPServer 대신 사용하면 된다.
    """
    pass
            
if __name__ == "__main__":
    HOST, PORT = "localhost", 50007
    # TCPServer 클래스를 사용해 소켓서버를 구동한다.
    # server.server_forever()로 소켓 서버가 구동 되며 하나의 클라이언트 접속 후 종료해도
    # 서버는 계속해서 다른 클라이언트 접속을 대기하고 처리한다.
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
    
    # TCPServer만 ThreadedTCPServer로 대체하면된다.
    # 이러면 여러 클라이언트의 요청을 동시에 처리할 수 있게 된다.
    
    # with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    #     server.serve_forever()