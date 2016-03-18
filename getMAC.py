#!/usr/bin/env python

import os, random
from os.path import expanduser
# have to give open an absolute path if it is to be run from anouther dir
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

if __name__ == '__main__':
    getRandom()
