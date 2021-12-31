# Overview
- 우분투, Linux 시스템에 vsftpd를 설치하는 방법

# vsftpd 설치
```shell
sudo apt-get install vsftpd
```

# /etc/vsfpd.conf 수정
```shell
sudo vim /etc/vsftpd.conf
```

```
write_enable=YES
local_umask=022
chroot_local_user=YES
allow_writeable_chroot=YES
pasv_enable=YES
pasv_min_port=10090
pasv_max_port=10100
```
- 서버 계정으로 FTP에 접속할 수 있도록 위 내용을 제일 하단에 추가한다.

# FTP 서비스 재시작
```shell
sudo systemctl restart vsftpd.service
```

# 방화벽 설정
- FTP 기본 포트인 21번 포트와 위에 설정에서 사용한 패시브 모드의 포트 범위인 10090-10100을 방화벽에서 허용하도록 설정한다.
