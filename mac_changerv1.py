#!usr/bin/env python

import subprocess
import time

interface = input("interface > ")
new_mac = input("nem mac > ")

print(f"[+] Changing MAC address of {interface} to {new_mac} ...")
time.sleep(1)
subprocess.call(["ifconfig", interface, "down"])
print("[+] " + interface + " is down")
time.sleep(1)
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
print("[+] Applying changes")
time.sleep(1)
subprocess.call(["ifconfig", interface, "up"])
print("[+] " + interface + " is up")
time.sleep(1)
print("[+] ...Confirming results... ")
subprocess.call(["ifconfig"])
