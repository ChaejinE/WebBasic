""" 
wsgiref : WSGI 프로그램 작성 시 사용하는 모듈

WSGI(Web Server Gateway Interface)는 웹 서버 소프트웨어와 파이썬으로 작성된
웹 응용 프로그램 간의 표준 인터페이스다.
쉽게 말해 웹서버가 클라이언트로부터 받는 요청을 파이썬 어플리케이션에 전달해서 실행하고, 그 실행결과를
돌려받기 위한 약속이다.
"""

from cgi import parse_qs

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