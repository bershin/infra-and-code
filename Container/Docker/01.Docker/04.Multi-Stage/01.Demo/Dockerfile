FROM node:22-alpine as build

WORKDIR /app

# Copy package.json and install dependencies first to leverage Docker cache
COPY package* .

# Install dependencies
RUN npm ci

FROM gcr.io/distroless/nodejs22

WORKDIR /app

COPY --from=build /app/node_modules node_modules

# COPY source dest
COPY src src

# Expose the port your application runs on
EXPOSE 3000

# Start the application
# CMD ["npm", "start"]
# distroless Node image, the entrypoint is already node.
CMD ["src/index.js"]