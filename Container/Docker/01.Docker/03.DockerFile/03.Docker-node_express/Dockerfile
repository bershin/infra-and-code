FROM node:22

WORKDIR /app

# Copy package.json and install dependencies first to leverage Docker cache
COPY package* .

# Install dependencies
RUN npm ci

# COPY source dest
COPY src/index.js index.js

# Expose the port your application runs on
EXPOSE 3000

# Start the application
# CMD ["npm", "start"]
CMD ["node", "index.js"]