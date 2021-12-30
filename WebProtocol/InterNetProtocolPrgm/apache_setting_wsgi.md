# 아파치에 WSGI 설정
```shell
sudo apt-get install libapache2-mod-wsgi-py3
```
- 아파치에서 WSGI를 사용하기 위해 mod_wsgi 모듈을 설치해야한다.

```shell
<VirtualHost *:8088>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        ScriptAlias /cgi-bin/ /var/www/cgi-bin/
        <Directory /var/www/cgi-bin>
          Options +ExecCGI
          AddHandler cgi-script .py
        </Directory>

        WSGIScriptAlias / /var/www/wsgi/wsgi.py
        <Directory /var/www/wsgi>
          <Files wsgi.py>
            Require all granted
          </Files>
        </Directory>
</VirtualHost>
```
- /etc/apache2/sites-enabled/000-default.conf 에 WSGI에 대한 설정을 추가한다.
- /로 요청되는 URL은 모두 wsgi.py 파일이 담당하게 된다.