#!/usr/bin/env python

# This is a random MAC address gen
# This is to be used with the 'macauto', 'macshow', 'macback' functions

from os.path import expanduser

import os, random, re, sys

def getRandom():
    home = expanduser("~")
    fileName = home+'/MACInstall/MACFormatted.txt'
    totalBytes = os.stat(fileName).st_size
    randomPoint = random.randint(0, totalBytes)
    file = open(fileName)
    file.seek(randomPoint)
    file.readline()
    MAC = file.readline()
    MAC = MAC.rstrip()
    return(MAC.lower())
    
def MACRand():
    """ This makes a random hexvalue, and return it fromatted such xx:xx:xx"""
    hexvals= ['0', '1', '2', '3', '4', '5', '6', '7', '8',
              '9', 'a', 'b', 'c', 'd', 'e', 'f']
    
    MAC = []
    for i in range(0,6):
        MAC.append(hexvals[random.randint(0,15)])
    MAC = ''.join(MAC)
    MAC = re.findall('..',MAC)
    MAC = ':'.join(MAC)
    print(getRandom()+":"+MAC)
    
if __name__ == '__main__':
    MACRand()
