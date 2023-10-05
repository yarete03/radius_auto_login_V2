import subprocess

def stop():
    subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", 'Invoke-WebRequest "https://pignatellif.edetronik.es/logout?"  -UseBasicParsing'])


def main():
    stop()


if __name__ == "__main__":
    main()