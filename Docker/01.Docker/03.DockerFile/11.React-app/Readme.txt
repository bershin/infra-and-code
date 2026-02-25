% npx create-react-app --template typescript containerize-react-app
% cd containerize-react-app
% npm start
http://localhost:3001
Edit "src/App.tsx" to see hot reloading.
Find the one responsible for serving the http request(WebpackDevServer).
For production build use "npm run build"
npx http-server@14.1.1 build
Hot reloading doesn't work use "npm run build & npx http-server@14.1.1 build" to load update

% docker build -t react-app:alpine .
% docker run --rm -it react-app:alpine sh