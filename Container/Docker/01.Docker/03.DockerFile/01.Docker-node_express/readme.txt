# Express app to create user and check them
% npm init -y # Create package.json file
% npm install express@4.19.2 body-parser@1.20.2 --save-exact # update package.json file
Write code in index.js
Update package.json to have start instead of test.
npm start
curl http://localhost:3000
Use postman to test the post request
% docker build -t express_app:v0.0.1 .
% docker run -p 3000:3000 --name expressapp  express_app:v0.0.1
