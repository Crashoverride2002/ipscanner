import argparse,subprocess
from array import array
import time
import unicodedata
import codecs
import platform
import time
import _xxsubinterpreters as subinterpreters
from threading import Thread
import textwrap as tw
import pickle
from queue import Queue
from string import Formatter
import sys


valid_ip = array('B')
valid_ip.append(1)
IP_RANGE = array('u')
SSIp = array('u')
ipsplit1 = array('u')
ipsplit2 = array('u')
encoding = 'utf-8'
f = open("Ips.net","w+")
def ping_ip(ip_address, count):
    #'''
    #Ping IP address and return tuple:
    #On success: (return code = 0, command output)
    #On failure: (return code, error output (stderr))
    #'''
    
    reply = subprocess.run(
        'ping {0}'.format( ip_address),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8'
    )
    if reply.returncode == 0:
        f.write("{0}\n".format(ip_address))
        
        print("Adding:{0} written#".format(ip_address))
        return True, reply.stdout
    else:
        return False, reply.stdout+reply.stderr



parser = argparse.ArgumentParser(description='Ping script')
print("Version {0} ".format(platform.python_version()))
parser.add_argument('-a', action="store", dest="ip")
parser.add_argument('-r', action="store", dest="ranges")
args = parser.parse_args()
print(args.ranges)
SSIp = args.ranges.split('-')

ipsplit1 = SSIp[0].split('.')
ipsplit2 = SSIp[1].split('.')
#print(ipsplit1)
#print(ipsplit2)
#print(args)
CountResult = 0
count4 = int(ipsplit2[3]) - int(ipsplit1[3])
count3 = int(ipsplit2[2]) - int(ipsplit1[2])
count2 = int(ipsplit2[1]) - int(ipsplit1[1])
count1 = int(ipsplit2[0]) - int(ipsplit1[0])
if (count4 > 0):
    CountResult = count4
if (count3 > 0):
    CountResult *= count3
if (count2 > 0):
    CountResult *= count2
if (count1 > 0):
    CountResult *= count1
print(CountResult)
ipaddr = "192.168.1.1"
x1 = range(int(ipsplit1[0]),int(ipsplit2[0]))
x2 = range(int(ipsplit1[1]),int(ipsplit2[1]))
x3 = range(int(ipsplit1[2]),int(ipsplit2[2]))
x4 = range(int(ipsplit1[3]),int(ipsplit2[3]))
if int(ipsplit1[0]) == int(ipsplit2[0]):
    x1 = int(ipsplit1[0])
if int(ipsplit1[1]) == int(ipsplit2[1]):
    x2 = int(ipsplit1[1])
if int(ipsplit1[2]) == int(ipsplit2[2]):
    x3 = int(ipsplit1[2])
if int(ipsplit1[3]) == int(ipsplit2[3]):
    x4 = int(ipsplit1[3])
print("count1: {0}".format(count1))
print("count2: {0}".format(count2))
print("count3: {0}".format(count3))
print("count4: {0}".format(count4))
if count1<=0:
    count1=ipsplit1[0]
if count2<=0:
    count2=ipsplit1[1]
if count3<=0:
    count3=ipsplit1[2]
#if count4<=0 or count4>int(ipsplit1[3]):
    count4=int(ipsplit1[3])


incounter = 0;
if valid_ip is None:
    valid_ip = []
while (incounter < CountResult):
    ipaddr = "{0}.{1}.{2}.{3}".format(count1,count2,count3,count4)
    if int(count4) >int(ipsplit2[3]):
        count4 = int(ipsplit1[3])
        count3 += 1
    if int(count3) >int(ipsplit2[2]):
        count3 = int(ipsplit1[2])
        count2 += 1;
    if int(count2) >int(ipsplit2[1]):
        count2 = int(ipsplit1[1])
        count1 += 1
    if int(count1) >int(ipsplit2[0]):
        count1 = int(ipsplit1[0])
    incounter +=1
    
    print("Calc : {0}.{1}.{2}.{3}".format(count1,count2,count3,count4))
    ipaddr = "{0}.{1}.{2}.{3}".format(count1,count2,count3,count4)
    print("ipAddr. {0}".format(ipaddr))
    rc, message = ping_ip(ipaddr, 1)
    time.sleep(2)
    count4 += 1
    
    print(message)
print("we are here.")
f.close()
    # rc, message = ping_ip(args.ip, args.count)

    