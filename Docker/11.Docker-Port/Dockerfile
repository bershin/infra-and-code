FROM nginx:alpine-slim

RUN mkdir -p /usr/share/nginx/html/app1
RUN mkdir -p /usr/share/nginx/html/app2

COPY index-app1.html /usr/share/nginx/html/app1/index.html
COPY index-app2.html /usr/share/nginx/html/app2/index.html
COPY index.html /usr/share/nginx/html/index.html

COPY nginx-index.conf /etc/nginx/conf.d/

EXPOSE 8081 8082