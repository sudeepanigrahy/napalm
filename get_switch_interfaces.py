import json
from getpass import getpass
from napalm import get_network_driver

def switch_interfaces(creds):
    driver=get_network_driver(creds[3])
    connection = driver(creds[0], creds[1], creds[2])
    connection.open()
    print("Connection to the switch is established...", '\n')

    if 'interface' in creds[4] or 'interfaces' in creds[4]:
        data_p = connection.get_interfaces()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        elif creds[6]:
            for i,j in data_p.items():
                if i.lower() == creds[6].lower():
                    print(f"Details of {i} are as follows:\n{j}")
        else: print("You can either select full view or a particular interface, run the code again and choose..")

if __name__=='__main__':
    switch = input("Gimme the Switch's Name or IP:\n")
    ios = input("Gimme the switch's os:\n")
    username = input("Gimme your username:\n")
    password = getpass()
    req = input("What do you want ?\n")
    view = input("Do you want the full view?\n")
    int_number = input("Any particular interface?\n")
    print('\n')
    creds = [switch, username, password, ios, req, view, int_number]
    switch_interfaces(creds)
    