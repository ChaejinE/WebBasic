"""
ftplib 모듈은 FTP 서버에 접속하고 파일을 다운로드 또는 업로드하기 위해서 사용하는 모듈이다.

FTP 서버의 루트 디렉토리에 data.txt 파일이 있다고 해보자.
data.txt 파일을 다운로드 받은 후 data.txt 파일의 숫자들의 평균을
계산하여 result.txt 파일에 쓰고, FTP 서버의 루트 디렉터리에 result.txt 파일을
저장해본다.
"""

import ftplib

# ftp = ftplib.FTP(host='52.78.8.xxx')

# ftp.set_pasv(False)

# ftp.login(user="username", passwd="pwd")
# ftp.dir()

# with open("data.txt", 'w') as save_f:
#     ftp.retrlines("RETR data.txt", save_f.write)

# FTP 서버의 ftp 객체를 생성한다.
with ftplib.FTP(host="your host ip") as ftp:
    # 패시브 모드를 False 로 설정한다.
    # 서버 설정에 따라 다르게 동작할 수 있으므로 오류가 난다면 True로 설정한다.
    # FTP 모드에는 Active mode, Passive mode가 있다.
    # Active mode는 Client가 Server에 접속을 하는 것이 아닌 Server가 Client에
    # 접속하는 방식이고 Passive mode는 이것의 반대라고 생각하면 된다.
    ftp.set_pasv(False)
    
    # 접속 가능한 계정가 비밀번호로 로그인을 수행한다.
    ftp.login(user="your user name", passwd="your_passwd")
    
    # 접속한 FTP에 어떤 파일들이 있는지 확인하려면 ftp.dir()을 호출하면된다.
    
    with open('data.txt', 'w') as save_f:
        # txt 파일은 아스키 파일이 아니므로 retrlines() 함수를 사용해 다운로드 할 수 있다.
        # 만약 바이너리 파일이라면 retlines 대신 retrbinary 함수를 사용해야하고 저장하기 모드도 wb를 사용하면된다.
        ftp.retrlines("RETR data.txt", save_f.write)
        
    with open("data.txt") as f:
        data = f.read()
        numbers = data.split()
        avg = sum(map(int, numbers)) / len(numbers)
        
    with open("result.txt", 'w') as f:
        f.write(str(avg))
        
    with open("result.txt", 'rb') as read_f:
        # FTP 서버로 파일을 저장할 경우 storelines를 사용하고, 'RETR' 대신 'STOR' 명령어를 사용하면된다.
        ftp.storlines("STOR result.txt", read_f)