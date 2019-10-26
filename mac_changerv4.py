#!usr/bin/env python

import subprocess
import time
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Choose interface to change MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="Type new MAC address.")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC address of " + interface + " to " + new_mac + " ...")
    time.sleep(1)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] " + interface + " is down")
    time.sleep(1)
    print("[+] Applying changes")
    time.sleep(1)
    print("[+] " + interface + " is up")
    time.sleep(1)
    print("[+] ...Confirming results... ")
    time.sleep(1)
    subprocess.call(["ifconfig"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)

