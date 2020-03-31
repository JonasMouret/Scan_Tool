import os
import re


def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    print (command)
    process = os.popen(command)
    results = str(process.read())
    return results
