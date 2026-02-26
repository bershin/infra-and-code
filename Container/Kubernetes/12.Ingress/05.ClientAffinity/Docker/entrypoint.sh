#!/bin/sh

h_name="$(hostname)"
h_ip="$(hostname -i | awk '{print $1}')"

sed -i "s/hostname/$h_name/g" /usr/share/nginx/html/index.html
sed -i "s/ip/$h_ip/g" /usr/share/nginx/html/index.html

nginx -g 'daemon off;'