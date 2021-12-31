import http.client
import urllib

params = urllib.parse.urlencode({'@name': '홍길동', '@age': 55})

headers = {"Content-type": "application/x-www-form-urlencoded"}

conn = http.client.HTTPSConnection("wikidocs.net")
conn.request("POST", "/", params, headers)

r = conn.getresponse()
print(r.status, r.reason)

print(r.read())