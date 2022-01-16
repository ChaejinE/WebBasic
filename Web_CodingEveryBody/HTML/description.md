# Tag
- 앞 : 열려있는 태그, 뒤 : 닫히는 태그

```html
<strong> ... </strong>
```
- ... 내용을 검은색 **굵은 글씨**로 강조 !

```html
<u> ... </u>
```
- ... 내용에 <u>밑줄</u> !

```html
<h1>HTML Practice</h1>

<p>
    My name is <strong>Chaejin Jeong</strong>
    <br>My id is <u>lotto</u>
</p>

<p style="margin-top:40px;">
    I'm trying to practice HTML
    <br>Easy ~~
</p>
```
- p tag : 인기있는 tag, Phase를 나눠준다.
- br tag : 2위 Tag, 줄바꿈

## Attribute
```html
<img src="..." width="100%">
```

# parent child
```html
<ul>
    <li>1. C</li>
    <li>2. C++</li>
    <li>3. Python</li>
</ul>
```
- li는 child, ul은 parent
- parent-child를 갖는 tag들이있다.
- 숫자 뺴려면 ul을 ol로 바꿔주면된다.
  - ol : Ordered List
  - ul : Unordered List
- li는 2대가 같이다닌다.

```html
<table>
    <tr>
        <td>head</td>
        <td>98i.1%</td>
    </tr>
    <tr>
        <td>body</td>
        <td>97.9%</td>
</table>
```
- td는 3대가 같이 다닌다.

# 문서구조 및 슈퍼스타 tag
```html
<title>Web1 -- html</title>
<meta charset="utf-8">
```
- 한국어와 같은 문자를 display 할때는 meta
- title은 문서의 제목이 된다.

```html
<!doctype html>
<html>
<head>
    ...
</head>

<body>
    ...
</body>
</html>
```
- HTML은 위의 틀을 약속으로하고 있다.

# html speicification
```html
<h1><a href="https://developer.mozilla.org/ko/docs/Web/HTML"
        target="_blank" title="html specification">HTML</a> Practice 할란다.</h1>
```
- a : anchor
  - href: 이 url을 참조한다.
  - target _blank : 새 웹부라우저 키면서 접속
  - title : 설명 정보

# 인터넷
- 인터넷은 두 대 이상의 컴퓨터가 있을 때 의미가 있다.
- Web Browser - Web Server (info.cern.ch)
  - Web Browser, Web Server는 인터넷으로 연결되어있다.
  - WebServer - index.html
- Web Browser - info.cern.ch/index.html을 입려하면 전기신호를 보내게된다.
- WebServer는 index.html에 대한 내용을 얻고 Web Browser에 쏜다.
- Web Browser는 받고, 읽어들인다.
- Web Browser .. request .. Client !!
- Web Server .. response .. Server !! 라고 부르게된다.