import os
import subprocess
from pynput import keyboard as kb

gw = "192.168.75.254"
my_pid = None
forbidden = ['Console', 'KB\\r\\n\'', 'KB\\r\\npython.exe', 'stdout=b\'python.exe']

def getting_pid(my_pid, forbidden):
    tasklist = subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", 'tasklist | findstr "python"'],
                              capture_output=True)
    tasklist = str(tasklist)
    tasklist = tasklist.split(',')
    tasklist = tasklist[4]
    tasklist = tasklist.split(' ')
    new_tasklist = []
    for i in tasklist:
        if i != '' and i not in forbidden:
            new_tasklist.append(i)
    if my_pid != None and my_pid == new_tasklist[0]:
        for i in range(3):
            new_tasklist.pop(0)
    return new_tasklist



def iping():
    path_to_profile_ps = "{}\\Documents\\WindowsPowerShell\\Microsoft.PowerShell_profile.ps1".format(os.path.expanduser('~'))
    try:
        open(path_to_profile_ps, "r")
    except FileNotFoundError:
        subprocess.run(["powershell","powershell -WindowStyle Hidden -Command Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"])
        profile_ps = open(path_to_profile_ps, "w")
        profile_ps.write('\n'
                         'Function New-IntervalPing {\n\n'
                         '    [Alias("iping")]\n'
                         '    Param(\n'
                         '        [string]$ComputerName,\n'
                         '        [int]$C = 1,\n'
                         '        [int]$T = 50,\n'
                         '        [int]$I = 50\n'
                         '    )\n\n'
                         '    1..$C | ForEach-Object {\n'
                         '        $Ping = [System.Net.NetworkInformation.Ping]::New()\n'
                         '        $Ping.Send($ComputerName,$T)\n'
                         '        start-sleep -Milliseconds $I\n'
                         '    }\n'
                         '}\n')
        profile_ps.close()

    ping = subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", "iping {}".format(gw)], capture_output=True)
    ping = str(ping)

    while "Success" not in ping:
        ping = subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", "iping {}".format(gw)], capture_output=True)
        ping = str(ping)



def first_time():
    iping()
    subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", "C:\\Users\\Yaret\\PycharmProjects\\auto_login\\auto_login.ps1"])


def main():

    def cleaner():
        new_tasklist = getting_pid(my_pid, forbidden)
        pids = []
        counter = 0
        for element in new_tasklist:
            if counter % 3:
                pass
            else:
                pids.append(element)
            counter += 1
        for pid in pids:
            subprocess.run(["powershell", 'powershell -WindowStyle Hidden -Command taskkill /pid {} /f'.format(pid)])

    def launcher():
        cleaner()
        iping()
        subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", "C:\\Users\\Yaret\\PycharmProjects\\auto_login\\auto_login.ps1"])


    def stop():
        cleaner()
        subprocess.run(["powershell", "powershell -WindowStyle Hidden -Command", "C:\\Users\\Yaret\\PycharmProjects\\auto_login\\stop.ps1"])

    hotkeys = {'<ctrl>+<shift>+ñ': launcher,
               '<ctrl>+<shift>+l': stop}


    with kb.GlobalHotKeys(hotkeys) as listener:
        listener.run()


if __name__ == "__main__":
    first_time()
    new_tasklist = getting_pid(my_pid, forbidden)
    my_pid = new_tasklist[0]
    main()