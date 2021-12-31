""" 
http.client 모듈은 HTTP 프로토콜의 클라이언트 역할을 수행하는 모듈이다.
이 모듈보다는 requests 모듈을 사용할 것은 권장하고 있다.

페이지 번호를 입력받아서 Wikidocs의 특정 page resource를 html 파일로 저장하는 함수를 작성한 예시다.
"""

import http.client

def get_wikidocs(page):
    # 사이트에 접속하기 위해 HTTPSConnection 객체를 생성한다.
    conn = http.client.HTTPSConnection("wikidocs.net")
    # /12 페이지 리소스를 GET 방식으로 요청한다.
    conn.request("GET", f"/{page}")
    r = conn.getresponse()
    print(r.status, r.reason) # 200 OK, 200 : 정상상태를 뜻하는 숫자값
    
    with open(f"./wikidocs_{page}.html", "wb") as f:
        # 데이터를 추출한다.
        f.write(r.read())
        print("Extract data")
        
    # conn 객체를 닫아준다.
    conn.close()
    
if __name__ == "__main__":
    get_wikidocs(12)



