"""
Banner Grabbing is a technique used to gain information about a remote server and is often used as part of a fingerprinting attack. Additionally, penetration testers sometimes use this as a technique to get information about remote servers.

requests module: https://requests.readthedocs.io/en/master/
sys module: https://docs.python.org/3/library/sys.html
json module: https://docs.python.org/3/library/json.html
socket module: https://docs.python.org/3/library/socket.html





"""









import sys 
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_ + "\n")

#ipinfo.io 

req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.loads(req_two.text)

print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
