import subprocess
import time
import optparse
import re

def change_mac(interface, new_mac):
    print("[+] Changing the interface " + interface + " to " + new_mac + " [+]")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig",interface, "up"])
    print("[+] Applying changes [+]")
    time.sleep(1)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Choose the interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="Choose the mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify and interface (--help for help)")
    elif not options.new_mac:
        parser.error("Please specify a mac address (--help for help)")
    return options

def get_current_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface])
    m_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res)
    if m_search:
        return  (m_search.group(0))
    else:
        print("[+] Can't find MAC address [+]")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("[+] Current MAC address: " + str(current_mac) + " [+]")
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address changed to: " + current_mac + "[+]")
else:
    print("[+] ERROR! MAC address not found")