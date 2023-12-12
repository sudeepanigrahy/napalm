import json
from napalm import get_network_driver

driver=get_network_driver('ios')
iosvl2=driver('****IP*****','****username*****','*****password****')
iosvl2.open()

ios_output = iosvl2.get_facts()
#ios_output = iosvl2.get_arp_table()
#ios_output = iosvl2.get_config()
#ios_output = iosvl2.get_environment()
#ios_output = iosvl2.get_interfaces()
#ios_output = iosvl2.get_interfaces_ip()
#ios_output = iosvl2.get_mac_address_table()
#ios_output = iosvl2.get_interfaces_counters()
#ios_output = iosvl2.get_users()
#ios_output = iosvl2.get_snmp_information()
#ios_output = iosvl2.get_vlans()
#ios_output = iosvl2.is_alive()

#json.dumps() is used to convert a python_dict into a json_object
#json.loads() is used to convert a json_object into a python_dict
jason = json.dumps(ios_output, sort_keys=True, indent=2)
print(jason)
iosvl2.close()
