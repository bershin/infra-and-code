#!/bin/sh

sed -i "s/POD_HOSTNAME/$(hostname)/g" /usr/share/nginx/html/index.html
sed -i "s/POD_IP/$(hostname -i)/g" /usr/share/nginx/html/app1/index.html

exec nginx -g 'daemon off;'