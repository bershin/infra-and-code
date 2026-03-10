FROM node:22

WORKDIR /app

COPY package*.json .

RUN npm ci

COPY src/index.js /app/

CMD ["node","index.js"]