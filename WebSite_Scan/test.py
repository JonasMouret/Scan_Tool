from ip_address import *


def gather_data(url):
    ip_address = get_ip_address(url)
    print (ip_address)
    return ip_address

gather_data('http://www.gravitr.com')