?? Why Ordering of instruction is importent and how to do it?
    - Reduce the build time by maximum using the cached layer
    - Put more stable command instructions on the begining of the dockerfile and commands likely to change in the end of the Dockerfile.

?? Demo: Prove ordering reduce the build time.
% docker build -t image-order:bad -f Dockerfile.bad .
Update index.js and run % docker build -t image-order:bad -f Dockerfile.bad .
Note "COPY . ." & "RUN np ci" runs again and take few seconds.

% docker build -t image-order:good -f Dockerfile.order .
Update index.js and run "docker build -t image-order:good -f Dockerfile.order ."
Note: only the copy command runs and will take few or zero miliseconds