FROM node:22-alpine

WORKDIR /app

COPY package*.json .

RUN npm ic

COPY . .

ENV PORT=5000
ENV APP_NAME="Test App"

CMD ["node", "src/index.js"]