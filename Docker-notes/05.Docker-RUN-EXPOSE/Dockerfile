FROM nginx:alpine-slim

COPY nginx-conf/*.conf /etc/nginx/conf.d/
COPY nginx-html/*.html /usr/share/nginx/html/

RUN apk --no-cache add curl

# EXPOSE 8080-8083
EXPOSE 8080 8081 8082 8083