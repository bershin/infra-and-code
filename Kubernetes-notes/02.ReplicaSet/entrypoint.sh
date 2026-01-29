#!/bin/sh

# Replace the placeholder with the actual hostname
sed -i "s/POD_HOSTNAME/$(hostname)/g" /usr/share/nginx/html/index.html

# Start the Nginx web server in the foreground
exec nginx -g 'daemon off;'
