- install nodemon@3.14 as development dependency & update package.json
    - % npm install nodemon@3.1.4 --save-exact --save-dev
    - update package.json script with dev
    - update CMD in Dockerfile
        npm start -> npm run start
        npm dev -> npm run dev
- Create bind mount in backend script and test using log & healthcheck
    - update startup-be.sh with bind mount
    - % docker logs -f backend
    - % curl http://localhost:3000/health
