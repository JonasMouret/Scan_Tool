#!/usr/bin/env python2

import  os

# Save all blocked Ips by fail2ban in a txt file
new_ips = os.system("sudo iptables -L -n | awk '$1==\"REJECT\" && $4!=\"0.0.0.0/0\" {print $4}' > /here/your/path/to/save/fail2ban.txt")

lines = []
with open('fail2ban.txt') as f:
    lines = [line for line in f if line.strip()]

with open ('saved_ban_ips.txt', 'a') as file:
    for i in lines:
		with open('saved_ban_ips.txt', 'rw' ) as f:
			if i not in f:
				file.write(i)
