#!/usr/bin/env python

import sys
import json
import subprocess
import xml.etree.ElementTree as ElementTree

from os import path
from os import chdir
from time import time
from base64 import b64encode
from datetime import datetime
from httplib import HTTPConnection
from httplib import HTTPSConnection

CONFIG_JSON_PATH = "config.json"
IP_FILE_PATH = "current_ip"

chdir(path.dirname(path.realpath(__file__)))

config_file = open(CONFIG_JSON_PATH)
config_list = json.load(config_file)
config_file.close()

print datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')

c = HTTPConnection("ip.changeip.com")
c.request("GET", "/")
res = c.getresponse()
data = res.read()
c.close()
if (res.status != 200  or res.reason != 'OK'):
    print 'Failed to get public IP Address...'
    sys.exit(1) # Maybe try another method if first fails

current_ip = data.split("\n")[0]
print 'WANIP: ' + current_ip

try:
    ip_file = open(IP_FILE_PATH)
    old_ip = ip_file.read().strip()
    ip_file.close()
except IOError:
    old_ip = ""

if current_ip != old_ip:
    print "Old ip: " + old_ip
    print "New ip: " + current_ip

    for config in config_list:
        c = HTTPSConnection("dynamicdns.park-your-domain.com")
        c.request("GET",
            "https://dynamicdns.park-your-domain.com/update?host=" + config['host'] +
            "&domain=" + config['domain'] +
            "&password=" + config['password'] + "&ip=" +current_ip
        )
        res = c.getresponse()
        data = res.read()
        c.close()
        if (res.status == 200 and res.reason == 'OK'):
            #print "Response: " + data
            xml = ElementTree.fromstring(data)
            if xml is not None:
                errcount = xml.find('ErrCount')
                #print 'ErrCount = ' + errcount.text
                if (errcount.text == '0'):
                    f = open(IP_FILE_PATH, "w+")
                    f.write(current_ip)
                    f.close()
                    print 'DNS Update successfull'
                else:
                    print 'Error: ' + xml.find('errors/Err1').text
            else:
                print 'Error: No xml data from update service...'
else:
    print "No change"
