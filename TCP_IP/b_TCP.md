# Overview
- Transmission Control Protocol, TCP, 전송제어프로토콜은 인터넷 프로토콜 스위트(IP)의 핵심 프로토콜중 하나로 IP와 함께 TCP/IP라는 명칭으로 불린다.
- 근거리 통신망이나 인트라넷, 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간 일련의 옥텟을 안정적으로, 순서대로, 에러 없이 교환할 수 있게 한다.
- TCP는 전송 계층에 위치한다.
  - 네트워크의 정보 전달을 통제하는 프로토콜이자 인터넷을 이루는 핵심 프로토콜의 하나이다.
- TCP는 웹 부라우저들이 www(world wise web)에서 서버에 연결할 때 사용되며 이메일 전송이나 파일 전송에도 사용된다.

# TCP
- OSI 7layer중 4계층에 해당한다.
- IP가 패킷들의 관계를 이해하지 못하고 그저 목적지를 제대로 찾아가는 것에 중점을 둔다면, TCP는 통신하고자 하는 양쪽 단말(endpoint)가 통신할 준비가 되었는지, 데이터가 제대로 전송되었는지, 데이터가 가는 도중 변질되지 않았는지, 수신자가 얼마나 받았고 빠진 부분은 없는지 등을 점검한다.
  - 이러한 정보는 TCP Header에 담겨있다.
  - SYN, ACK, FIN, RST, SOurce Port, Destination Port, Sequence Number, Window size, checksum 등 신뢰성 보장과 흐름제어, 혼잡 제어에 관여할 수 있는 요소들로 포함되어있다.
  - IP Header와 TCP Header를 제외한 TCP가 실을 수 있는 데이터 크기를 Segment라고 부른다.

![image](https://user-images.githubusercontent.com/69780812/147441038-328f103d-3283-474f-8ee0-1bf4a321135c.png)
- TCP는 IP의 정보 뿐 아니라 Port를 이용해 연결한다.
- 한쪽 Endpoint에 도착한 데이터가 어느 port로 들어가야하는지 알아야 연결을 시도할 수 있기 때문이다.
  - 위의 TCP Header를 보면 Soucre port, Destination Port를 확인할 수 있다.
  - 예를들어 양쪽 단말이 HTTP로 이루어진 문서를 주고받고자 하는 경우 데이터 통신을 하려면 Endpoint의 3306 port도 아니고 21 port도 아닌 80port로 연결해야한다.

# TCP 작동 3-way hand shake
- TCP를 사용하는 송신자와 수신자는 데이터 송수신전 서로 통신이 가능한지 확인한다.
  - 신뢰성있는 통신을 하기 위함이다.

```
1. 전화 번호를 누른다. 상대방의 전화기가 꺼져있지 않으면 연결음이 들리면서 연결을 시도한다.
2. 상대방이 전화를 받았고, 상대방의 목소리가 잘들린다.
3. 여러분은 "여보세요?" 한 마디와 함께 상대방이 자신의 목소리가 잘들리는지 확인한 후 대화를 시작한다.
```

```
1. 송신자가 수신자에게 "SYN"을 날려 통신이 가능한지 확인한다.
(이때, Port가 열려있어야한다.)
2. 수신자가 송신자로부터 "SYN"을 받고 "SYN/ACK"을 송신자에게 날려 통신할 준비가 되었음을 알린다.
3. 송신자가 수신자의 "SYN/ACK"를 받고 "ACK"를 날려 전송을 시작함을 알린다.
```
- TCP도 이전전의 예와 동일하게 작동한다. 다만, TCP Header 내 **SYN, SYN/ACK, ACK** flag를 사용해 통신을 시도한다.
  - 이것을 **3-way handshake**라고 부른다.

![image](https://user-images.githubusercontent.com/69780812/147449683-ddda9eac-1849-4377-9b8b-e82fd0d58d3a.png)
- TCP로 이루어지는 모든 통신은 반드시 3-way handshake을 통해 시작한다.
- 수신자가 받을 생각이 있는지, 준비가 되었는지, 송신자가 보낼 준비가 되었는지를 미리확인한 후 통신을 시작해 데이터를 안전하게 보내는 것이다.
- 데이터를 받으면 잘 받았다는 "ACK"를 송신자에 날린다.
- 송신자는 이 'ACK'를 보고 수신자가 데이터를 잘 받았음을 확인하고 다음 데이터를 전달할 준비를 한다.
- 이밖에 주로 사용하는 flag로는 RST, FIN, FIN/ACK, PUSH 등이 있는데 너무 길어지니 생략한다.

# TCP의 특징
![image](https://user-images.githubusercontent.com/69780812/147450227-93b41b6f-6959-438f-9f15-ca6be4832dc2.png)
- 연탄 배송을 생각해보면 연탄을 전달하는 사람은 받는 사람이 얼마나 받을 수 있는지 확인한 후 에 전달한다.확인을 안하면 연탄을 받는 입장에서 손에 들고 있는 연탄이 있으니 받을 수 없어 전달하려는 연탄이 깨지고 말 것이다. TCP도 마찬가지다.

## 1. 흐름 제어
- 송신자는 자신이 한 번에 얼마나 보낼 수 있는지, 수신자는 자신이 데이터를 어디까지 받았는지 끊임없이 확인하고 TCP Header 내의 "Window size"를 사용해 한번에 받고/보낼 수 있는 데이터의 양을 정한다.
  - window : 일정량의 데이터를 말한다.
  - 받는 쪽이 더 중요하니 window size는 수신자가 정한다. (3-way handshake 때 정한다.)
  - 그리고 자신의 상황에 따라 window size를 조절한다.
  - 이후 자신이 지금까지 받은 데이터 양을 확인해 송신자에게 보내는데, 이를 **Ackowledgement Number**라고 한다.
  - 수신자가 300번째 데이터를 받았으면 Ackowledgement Number에 1을 추가하여 301을 보낸다.
  - 300번까지 받았으니 301번 부터 보내라는 뜻이다.
  - 이 데이터의 순서 번호를 표기한 것이 바로 **Sequence Number**다.

## 2. 혼잡 제어
- 데이터를 주고 받는 양 단말도 중요하지만 데이터가 지나가는 네트워크 망의 혼잡 또한 중요하다.
- 다양한 방법이있지만 Slow Start에 대해 알아보자.
- 연결 초기 송신자와 수신자가 데이터를 넉넉히 주고 받을 준비가 되어있더라도 중간 경로인 네트워크가 혼잡하면 제대로 보낼 수 없을 것이다.
  - 송신자는 연결 초기에 데이터 송출량을 낮게 잡고 보내면서 수신자의 수신을 확인하며 데이터 송출량을 조금씩 늘린다.
  - 현재 네트워크에서 가장 적합한 데이터 송출량을 확인할 수 있게 된다. 이것이 **Slow Start**이다.
