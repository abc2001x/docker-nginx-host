#!/bin/sh
nginxPath="/var/run/nginx.pid"

if [ -f "$nginxPath" ]; then
	/usr/sbin/nginx -s reload
else
	/usr/sbin/nginx
fi

dnsmasq -q -8 /tmp/dnsmasq.log --port 53 -R -u root

python /hosts.py
