import subprocess
from time import sleep as sp

username = "21746204A"
passwd = "TDhJEWe4"

def auto_login():
    '''subprocess.run('curl --header "Host: pignatellif.edetronik.es" '
                   '-A "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0" '
                   '--header "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" '
                   '--header "Accept-Language: en-US,en;q=0.5" '
                   '--header "Accept-Encoding: gzip, deflate, br" '
                   '--header "Connection: keep-alive" '
                   '--header "Upgrade-Insecure-Requests: 1" '
                   '--header "Sec-Fetch-Dest: document" '
                   '--header "Sec-Fetch-Mode: navigate" '
                   '--header "Sec-Fetch-Site: none" '
                   '--header "Sec-Fetch-User: ?1" '
                   '-u {}:{} https://pignatellif.edetronik.es/login -i http -v'.format(username, passwd))'''
    subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", 'Invoke-WebRequest "https://pignatellif.edetronik.es/logout?"  -UseBasicParsing'])
    subprocess.run(["powershell", 'Invoke-WebRequest -Uri "https://pignatellif.edetronik.es/login?" -Method Post -Body @{username="' + username + '";password="' + passwd + '"} -ContentType "application/x-www-form-urlencoded" -UseBasicParsing'])
    sp(14400)
    auto_login()


def main():
    auto_login()


if __name__ == '__main__':
    main()