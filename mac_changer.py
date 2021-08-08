#!/usr/bin/env python2

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest= "interface", help= "interface of the script")
    parser.add_option("-m", "--mac", dest= "new_mac", help= "new mac address")
    (options,arguments) = parser.parse_args()
    if(not options.interface):
        parser.error("[-] enter interface")
    elif(not options.new_mac):
        parser.error("[-] enter new MAC")
    else:
        return options

def change_mac(interface, new_mac):
    print("[+] changing MAC of "+interface+" to "+new_mac)
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig",interface, "hw", "ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] MAC changed successfully") \

def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if (not current_mac):
        print("[-] cannot read mac addr")
    else:
        print(current_mac.group(0))
        return(current_mac.group(0))



options = get_arguments()
change_mac(options.interface, options.new_mac)
get_mac(options.interface)

if(options.new_mac == get_mac()):
    print("mac changed success")
