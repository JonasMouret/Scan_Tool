import os
import re

def get_ip_address(url):
    if url.startswith('http'):
        new_url = url.replace("http://","")
    if url.startswith('https'):
        new_url = url.replace("https://", "")
    command = "host " + new_url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find("has address") + 12
    return results[marker:].splitlines()[0]
