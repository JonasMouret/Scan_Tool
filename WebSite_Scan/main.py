from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *


print ('-' * 60)
print('Welcome in Site Scanner Alpha')
print ('-' * 60)

a = input('Please enter the name of the directory you-d like to save gather data : ')
b = input ("Please enter the name of the company that you're going to scan : ")
c = input("Please enter the address of the website you'd like to attack : ")

ROOT_DIR = a
create_dir(ROOT_DIR)

def gather_data(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap('-F ' + ip_address)
    robot_txt = get_robot_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robot_txt, whois)

def create_report(name, full_url, domain_name, nmap, robot_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robot_txt.txt', robot_txt)
    write_file(project_dir + '/whois.txt', whois)



gather_data(b, c)
