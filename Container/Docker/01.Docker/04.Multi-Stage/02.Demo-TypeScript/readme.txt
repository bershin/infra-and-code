% npm i --save-dev --save-exact typescript@5.5.3 @types/express@4.17.21
% npx tsc --init
% mv index.js index.ts
update tsconfig.json output the build artifact to "dist"
update package.json with build tsc -> should be in .bin folder
% npm run build
% PORT=3000 node dist/index.js
Update Dockerfile 
% docker build -t type-script-example .
% docker run --rm -e PORT=3000 -d -p 3008:3000 type-script-example 