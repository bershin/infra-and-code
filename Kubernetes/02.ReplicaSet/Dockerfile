# Use an official Nginx image as a parent image
FROM nginx:alpine

# Remove the default Nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy the static website's content to the Nginx html folder
COPY index.html /usr/share/nginx/html/

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# The container will start by executing the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
