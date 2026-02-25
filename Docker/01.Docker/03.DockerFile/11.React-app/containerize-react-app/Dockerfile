# 1. Bundle our production bundle
FROM node:22-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 2. Serve the bundle with http-server
FROM nginx:1.27.0
WORKDIR /usr/share/nginx/html
COPY --from=builder /app/build .
