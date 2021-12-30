""" 
wsgiref : WSGI 프로그램 작성 시 사용하는 모듈

WSGI(Web Server Gateway Interface)는 웹 서버 소프트웨어와 파이썬으로 작성된
웹 응용 프로그램 간의 표준 인터페이스다.
쉽게 말해 웹서버가 클라이언트로부터 받는 요청을 파이썬 어플리케이션에 전달해서 실행하고, 그 실행결과를
돌려받기 위한 약속이다.
"""

from cgi import parse_qs
from wsgiref.simple_server import demo_app, make_server

def application(environ, start_response):
    """envirion, start_response을 수신하고 리스트 형태의 바이트 문자열을 리턴하는 함수

    Args:
        environ ([dict]): HTTP 요청에 대한 정보와 OS or WSGI 서버의 설정등이 정의되어있는 딕셔너리
        start_response ([fucntion]): 일종의 Callback Function, 응답 상태코드와 HTTP헤더를 설정하는 역할

    Returns:
        [list]: 바이트 문자열을 리스트형태로 Return
    """
    
    # URL로 전달받은 인자 a, b를 얻기위해 QUERY_STRING에 해당하는 값을 parsing
    # 편리하게 파싱하기 위해 cgi의 parse_qs 함수 사용
    # 파라미터는 동일한 이름에 여러개의 값이 전달될 수 있어 리스트 형태로 정의된다.
    # 따라서 a param을 얻기 위해서는 첫번째 값만 얻을 수 있게한다.
    # get('a', [0])의 [0]은 a파라미터가 요청해서 생략되었을 경우의 default value다.
    params = parse_qs(environ["QUERY_STRING"])
    a = params.get('a', [0])[0]
    b = params.get('b', [0])[0]
    result = int(a) * int(b)
    
    status = '200 OK' # HTTP Status
    headers = [("Content-type", "text/plain; charset=utf-8")] # HTTP Headers
    # Return 하기 전에 반드시 먼저 호출해줘야한다.
    start_response(status, headers)
    
    return [f"Result:{result}".encode('utf-8')]

if __name__ == "__main__":
    # 이와 같은 간단한 wsgi server는 운영환경에서 적합하지 않으므로 테스트용으로만 사용해야한다.
    # 아파치 같은 웹서버 도움 없이도 WSGI 서버를 구동할 수 있다.
    with make_server('', 8088, application) as httpd:
        print("Serving on port 8088...")
        httpd.serve_forever()
        
    """ 
    django & Flask
    파이썬으로 만들어진 유명한 web framework이다.
    이들 역시 WSGI 규약에 맞게 개발된 파이썬 웹 애플리케이션이다.
    장고 설치시 wsgi.py파일이 설치되는 것을 확인할 수 있다.
    """