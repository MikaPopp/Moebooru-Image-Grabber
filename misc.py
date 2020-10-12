from __future__ import unicode_literals
import os
import psutil

def checkDiskSpace():
    path = "/"
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
    return gigabytes_avail

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def printAwesomeASCII():
    os.system("cls")
    print("\u001b[31;1m" + " __ __  _  _         ___                 ")
    print("\u001b[31;1m" + "|  \  \<_>| |__ ___ | . \ ___  ___  ___  ")
    print("\u001b[31;1m" + "|     || || / /<_> ||  _// . \| . \| . \ ")
    print("\u001b[31;1m" + "|_|_|_||_||_\_\<___||_|  \___/|  _/|  _/ ")
    print("\u001b[31;1m" + "                              |_|  |_|   ")
    print("\u001b[32m" + "Start grabbing...")