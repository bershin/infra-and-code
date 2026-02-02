FROM nginx:alpine-slim

COPY app.conf /etc/nginx/conf.d/app.conf
COPY index.html /usr/share/nginx/html/

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# The container will start by executing the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 8080