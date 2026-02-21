#!/bin/sh

sed -i "s/POD_HOSTNAME/$(hostname)/g" /usr/share/nginx/html/index.html

exec nginx -g 'daemon off;'