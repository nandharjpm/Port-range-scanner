import socket,time

fig="""
                        _ _                               _
                       | | |                             | |
  _ __   __ _ _ __   __| | |__   __ _    _ __   ___  _ __| |_    ___  ___ __ _ _ __  _ __   ___ _ __
 | '_ \ / _` | '_ \ / _` | '_ \ / _` |  | '_ \ / _ \| '__| __|  / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
 | | | | (_| | | | | (_| | | | | (_| |  | |_) | (_) | |  | |_   \__ \ (_| (_| | | | | | | |  __/ |
 |_| |_|\__,_|_| |_|\__,_|_| |_|\__,_|  | .__/ \___/|_|   \__|  |___/\___\__,_|_| |_|_| |_|\___|_|
                                        | |
                                        |_|
"""
print(fig)
time.sleep(2)
print()
domain=input("Enter Your Target Domain Name : ")
ip=socket.gethostbyname(domain)
srange=int(input("Enter the starting range of port : "))
erange=int(input("Enter the ending range of port : "))

for port in range(srange,erange+1):
    s = socket.socket()
    s.settimeout(1)
    res = s.connect_ex((ip, port))
    if res == 0:
        print(port, "open in", ip)
    else:
        print(port," is closed")
    s.close()
