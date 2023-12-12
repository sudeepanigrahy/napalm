import json
from getpass import getpass
from napalm import get_network_driver

def switch_facts(creds):
    driver=get_network_driver(creds[3])
    connection = driver(creds[0], creds[1], creds[2])
    connection.open()
    print("Connection to the switch is established...", '\n')

    if 'serial' in creds[4] and 'number' in creds[4]:
        data_p = connection.get_facts()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        else: print(f"Serial Number of this Switch is: {data_p['serial_number']}")

    if 'model' in creds[4]:
        data_p = connection.get_facts()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        else: print(f"Model of this Switch is: {data_p['model']}")
    
    if 'os' in creds[4] and 'version' in creds[4]:
        data_p = connection.get_facts()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        else: print(f"OS Version of this Switch is: {data_p['os_version']}")

    if 'uptime' in creds[4]:
        data_p = connection.get_facts()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        else: print(f"Uptime of this Switch is: {data_p['uptime']}")
    
    if 'vendor' in creds[4]:
        data_p = connection.get_facts()
        data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='yes' or creds[5]=='y' or creds[5]=='Y' or creds[5]=='Yes':
            print(data_j, '\n')
        else: print(f"Vendor of this switch is: {data_p['vendor']}")

    connection.close()

if __name__=='__main__':
    switch = input("Gimme the Switch's Name or IP:\n")
    ios = input("Gimme the switch's os:\n")
    username = input("Gimme your username:\n")
    password = getpass()
    req = input("What do you want ?\n")
    view = input("Do you wanna see the whole view?\n")
    print('\n')
    creds = [switch, username, password, ios, req, view]
    switch_facts(creds)

