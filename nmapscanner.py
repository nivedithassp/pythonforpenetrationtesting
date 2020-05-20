"""
Suggested readings:

The sys module and sys.argv:

https://python101.pythonlibrary.org/chapter20_sys.html
http://effbot.org/librarybook/sys.htm
https://pythonprogramming.net/sys-module-python-3/

More about python-nmap:

https://xael.org/pages/python-nmap-en.html
https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
"""
import nmap 
import sys 

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080]

scan_v = nmap.PortScanner()

print("\nScanning",target,"for ports 21,22,80,139,443 and 8080...\n")

for port in ports:
    portscan = scan_v.scan(target,str(port))
    print("Port",port," is ",portscan['scan'][list(portscan['scan'])[0]]['tcp'][port]['state']) #output in the form of dictionary

print("\nHost",target," is ",portscan['scan'][list(portscan['scan'])[0]]['status']['state'])
