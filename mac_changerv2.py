#!usr/bin/env python

import subprocess
import time
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Select interface to change MAC address.")
parser.add_option("-m", "--mac", dest="new_mac", help="Choose new MAC address.")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

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