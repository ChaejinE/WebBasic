# Overview
- Internet Protocol Suite : 인터넷 프로토콜 스위트, 인터넷에서 컴퓨터들이 서로 정보를 주고 받는 데 쓰이는 통신 규약 모음이다.
- Internet Protocol Suite 중 TCP와 IP가 가장 많이 쓰여 TCP/IP 프로토콜 슈트라고 불린다.
- TCP/IP는 하나의 프로토콜이 아닌 TCP와 IP를 합쳐서 부르는 말이다.
  - TCP : 전송 조절 프로토콜, IP위에서 동작하는 프로토콜로 데이터의 전달을 보증하고 보낸 순서대로 받게 해준다.
  - IP : 패킷 통신 방식의 인터넷 프로토콜, 패킷 전달 여부를 보중하지 않고 패킷을 보낸 순서와 받는 순서가 다를 수 있다.
  - HTTP, FTP, SMTP 등 TCP를 기반으로 한 많은 수의 애플리케이션 프로토콜들이 IP 위에서 동작하므로 묶어서 TCP/IP로 부르기도한다.
- TCP/IP를 사용하겠다는 것은 IP 주소 체계를 따르고 IP Routing을 이용해 목적지에 도달해 TCP의 특성을 활용하여 송신자와 수신자의 논리적 연결을 생성한다. 더나아가 신뢰성을 유지할 수 있도록 하는 것을 의미한다.
- 즉, TCP/IP를 말한다는 것은 **송신자가 수신자에게 IP 주소를 사용해 데이터를 전달**하고, 그 **데이터가 제대로 갔는지, 너무 빠르지는 않은지, 제대로 받았다고 연락은 오는지에 대한 이야기를 하는 것**이다.

## Trasport Layer(4Layer)
- 송신자와 수신자의 논리적 연결 (Connection)을 담당하는 부분
- 신뢰성 있는 연결을 유지하도록 도와준다.
- Endpoint(User)간의 연결을 생성학 ㅗ데이터를 얼마나 보냈는지 얼마나 받았는지 제대로 받았는지 등을 확인한다.
- TCP, UDP가 대표적이다.

## Network Layer(3 Layer)
- IP(Internet Protocol)이 활용되는 부분
- 한 Endpoint(User)가 다른 Endpoint로 가고자 할 경우 경로와 목적지를 찾아준다.
  - 이를 Routing이라 하며 대역이 다른 IP들이 목적지를 향해 제대로 찾아갈 수 있ㄴ도록 돕는 역할을 한다.

![image](https://user-images.githubusercontent.com/69780812/147437875-b4931a35-9d9c-493b-bf84-ae76ad0b9359.png)
- 우리가 인터넷에서 무언가 다운로드할 때 중간에 끊기거나 빠지는 부분 없이 완벽하게 받을 수 있는 이유가 TCP의 이러한 특성, **데이터가 빠지지 않고 제대로 전달됬는지를 챙기는 꼼꼼함 덕분**이다.
  - 이는 HTTP, HTTPS, FTP, SMTP 등과 같이 데이터를 안정적으로 모두 보내는 것을 중요시 하는 프로토콜의 기반이 되는 이유다.
- TCP를 기반으로 하는 프로토콜들은 TCP의 3-way handshake을 거친 후 각자 프로토콜(Layer7)에 기반한 교환 과정을 실시한다.

![image](https://user-images.githubusercontent.com/69780812/147440582-1a4a126c-a09a-4adc-a0c1-0ecd3955e56f.png)
- 위 이미지는 TCP 기반 프로토콜인 HTTPS의 SSL handshake를 도식화한 것이다.
  - TCP는 Layer4, HTTPS는 Layer7이다.
  - 파란색 : TCP '3-way handshake'
  - 노란색 : HTTPS 'SSL handshake'
  - HTTPS는 TCP 기반 프로토콜이라 SSL handshake에 앞서 3-way handshake를 실시하는 것을 알 수 있다.
