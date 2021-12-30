# 아파치 설치 및 설정
```shell
sudo apt-get install apache2
```

## port 변경
- /etc/apache2/ports.conf

```shell
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 8088

<IfModule ssl_module>
        Listen 8443
</IfModule>

<IfModule mod_gnutls.c>
        Listen 8443
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```
- HTTP 기본 포트 80, SSL 기본포트 443 대신 다른 포트를 사용해야하면 위처럼 바꾼다.

## CGI Setting
```shell
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
```
- 아파치가 파이썬 프로그램을 호출하려면 위와 같은 설정이 필요하다.
- ScriptAlias
  - http://52.78.8.100:8088/cgi-bin/multiple.py와 같은 /cgi-bin/으로 시작되는 URL을 호출했을 때 /var/www/cgi-bin/ 디렉터리의 파일을 읽게하는 설정이다.
  - 웹 브라우저에서 http://52.78.8.100:8088/cgi-bin/multiple.py URL을 호출하면 서버의 /var/www/cgi-bin/multiple.py 파일이 ㅎ출될 것이다.

```shell
<Directory /var/www/cgi-bin>
    Options +ExecCGI
    AddHandler cgi-script .py
</Directory>
```
- /var/www/cgi-bin 디렉터리는 위와 같이 설정해야한다.
- Options +ExecCGI는 /var/www/cgi-bin 디렉터리가 CGI 파일을 실행할 수 있는 경로라는 의미다.
- AddHandler cgi-script .py : CGI 파일로 .py 확장자에 해당되는 python script를 사용하겠다는 의미다.

```shell
<VirtualHost *:8088> # 80 port를 8088로 변경
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    ScriptAlias /cgi-bin/ /var/www/cgi-bin/
    <Directory /var/www/cgi-bin>
        Options +ExecCGI
        AddHandler cgi-script .py
    </Directory>
</VirtualHost>
```
- 이전에 설정하려했던 CGI 설정들을 적용하려면 아파치의 파일을 수정해야한다.
  - **/etc/apache2/sites-enabled/000-default.conf**
- 80 port 대신 8088fh qusrudgoTekaus <\VirtualHost *:8088>로 변경해준다.

```shell
cd /etc/apache2/mods-enabled
sudo ln -s ../mods-available/cgi.load
```
- 아파치가 cgi 기능을 할 수 있도록 cgi.load 파일을 enable 해준다.

```shell
cd /var/www/
sudo mkdir cgi-bin
sudo mv path.../multiple.py /var/www/cgi-bin
```
- 작성한 multiple.py 를 /var/www/cgi-bin 디렉터리로 이동한다.

```shell
cd /var/www/cgi-bin
chmod a+x multiple.py
```
- CGI 파일은 아파치가 실행할 수 있도록 실행권한을 준다.

```shell
sudo systemctl restart apache2.service
```
- 설정이 바뀌었기 때문에 아파치를 재시작해준다.