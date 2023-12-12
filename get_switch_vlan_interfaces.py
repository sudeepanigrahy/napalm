import json
from getpass import getpass
from napalm import get_network_driver

def switch_vlan_interfaces(creds):
    driver=get_network_driver(creds[3])
    connection = driver(creds[0], creds[1], creds[2])
    connection.open()
    print("Connection to the switch is established...", '\n')

    if 'vlan' in req or 'vlans' in req:
        data_p = connection.get_vlans()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        else: 
            print(f"Name of the vlan {creds[6]} is '{data_p[creds[6]]['name']}'....and...\n")
            print(f"The interfaces under the vlan {creds[6]} is/are:\n{data_p[creds[6]]['interfaces']}")



if __name__=='__main__':
    switch = input("Gimme the Switch's Name or IP:\n")
    ios = input("Gimme the switch's os:\n")
    username = input("Gimme your username:\n")
    password = getpass()
    req = input("What do you want ?\n")
    view = input("Do you wanna see the whole view?\n")
    vlan_specific = input("Any vlan in particular whose interfaces you wanna see ?\n")
    print('\n')
    creds = [switch, username, password, ios, req, view,  vlan_specific]
    switch_vlan_interfaces(creds)