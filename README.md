# mac_changer.py

Process of creating a mac changer script for linux OS.

From v0 to v5 (v5 has comments expaining the code) shows the improvements on the script in terms of new objects, modules, functions and also cleaner code.

Final version is "mac_changer.py"

Why changing MAC address?
1) Increase anonymity
2) Impersonate other devices
3) Bypass filters

Usage:
  -i or --interface to select interface
  -m or --mac to choose new mac address
  python mac_changer.py -i <interface> -m <new mac>
  Ex: python mac_changer.py --interface eth0 --mac 00:11:22:33:44:55
  
