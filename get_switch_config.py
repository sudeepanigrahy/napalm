import json
from getpass import getpass
from napalm import get_network_driver

def switch_config(creds):
    driver=get_network_driver(creds[3])
    connection = driver(creds[0], creds[1], creds[2])
    connection.open()
    print("Connection to the switch is established...", '\n')

    if 'config' in creds[4]:
        data_p = connection.get_config()
        #data_j = json.dumps(data_p, sort_keys=True, indent=4)
        if creds[5]=='running':
            print(data_p["running"], '\n')
        elif creds[5]=='startup':
            print(data_p["startup"], '\n')
        else: print("You can either select startup or running config, run the code again and choose..")

if __name__=='__main__':
    switch = input("Gimme the Switch's Name or IP:\n")
    ios = input("Gimme the switch's os:\n")
    username = input("Gimme your username:\n")
    password = getpass()
    req = input("What do you want ?\n")
    config_type = input("Which config do you want- running or startup?\n")
    print('\n')
    creds = [switch, username, password, ios, req, config_type]
    switch_config(creds)

