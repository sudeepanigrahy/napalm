import json
from getpass import getpass
from napalm import get_network_driver

def switch_arp(creds):
    driver=get_network_driver(creds[3])
    connection = driver(creds[0], creds[1], creds[2])
    connection.open()
    print("Connection to the switch is established...", '\n')

    if 'arp' in creds[4]:
        data_p = connection.get_arp_table()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        elif creds[6]:
            for i in data_p:
                if i["ip"]==creds[6]:
                    print(f"The arp cache of the required IP is:\n {i}")
        else: print("You can either see the whole arp-cache or for a single IP, run the code again and choose..")

if __name__=='__main__':
    switch = input("Gimme the Switch's Name or IP:\n")
    ios = input("Gimme the switch's os:\n")
    username = input("Gimme your username:\n")
    password = getpass()
    req = input("What do you want ?\n")
    view = input("Do you wanna see the whole view?\n")
    ip = input("Any IP in particular?\n")
    print('\n')
    creds = [switch, username, password, ios, req, view, ip]
    switch_arp(creds)

