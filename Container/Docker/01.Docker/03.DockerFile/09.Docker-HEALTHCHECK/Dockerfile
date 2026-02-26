FROM nginx:alpine-slim

COPY index.html /usr/share/nginx/html/

RUN apk --no-cache add curl

HEALTHCHECK --interval=30s --start-period=5s --start-interval=5s --timeout=30s --retries=3 CMD curl -f http://localhost/ || exit 1
