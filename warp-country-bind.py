## warp-country-bind.py
## Python script for country binding (i need Poland for use) 
import requests
import re
import sys
import subprocess

p = re.compile(r'[a-zA-Z]+')
cloudflare_ips = ['162.159.192.1','162.159.193.1','162.159.192.2','162.159.193.2','162.159.192.3','162.159.193.3','162.159.192.4','162.159.193.4','162.159.192.5','162.159.193.5','162.159.192.6','162.159.193.6', '162.159.192.7','162.159.193.7','162.159.192.8','162.159.193.8','162.159.192.9','162.159.193.9']
port = ':2408'
country_code = requests.get('http://ipinfo.io/country')
data = [x.strip() for x in re.findall(p, country_code.text)]
clearcountry = data[0]
if clearcountry=='PL':
                    sys.exit()   
else: 
        for i in range(len(cloudflare_ips)):
            ip_port=cloudflare_ips[i]+port
            subprocess.run(["warp-cli", "set-custom-endpoint", ip_port],stdout=subprocess.DEVNULL)
            delay = 3000
            country_code = requests.get('http://ipinfo.io/country')
            data = [x.strip() for x in re.findall(p, country_code.text)]
            clearcountry = data[0]
            if clearcountry=='PL':
                    sys.exit()  
