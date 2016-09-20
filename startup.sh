#!/bin/sh
/usr/sbin/nginx
dnsmasq -q -8 /tmp/dnsmasq.log --port 53 -R -u root

python /hosts.py
