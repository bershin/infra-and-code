ENTRYPOINTis used to specify the main executable for the container which is not intended to be overridden, while CMD is used to provide default arguments for that executable, which are easily overridden by the user at runtime.

% docker build -t cmd-example -f Dockerfile.cmd .
% docker run --rm cmd-example
Hello from CMD in Dockerfile.cmd
% docker run --rm cmd-example echo "hello from cmd in terminal"
hello from cmd in terminal
% docker run --rm cmd-example sh -c "apk add curl && curl http://google.com"
fetch https://dl-cdn.alpinelinux.org/alpine/v3.20/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.20/community/aarch64/APKINDEX.tar.gz
(1/10) Installing ca-certificates (20250911-r0)

% docker build -t entrypoint-example -f Dockerfile.entrypoint .
% docker run --rm entrypoint-example 
Hello from ENTRYPOINT in Dockerfile.entrypoint
% docker run --rm entrypoint-example  "Hello from terminal"
Hello from ENTRYPOINT in Dockerfile.entrypoint Hello from terminal
% docker run --rm entrypoint-example  echo "Hello from terminal"
Hello from ENTRYPOINT in Dockerfile.entrypoint echo Hello from terminal
% docker run --rm --entrypoint "echo" entrypoint-example  "hello with cmd+entry"
hello with cmd+entry

% docker build -t cmd-entrypoint-example . 
% docker run --rm cmd-entrypoint-example
default message
% docker run --rm cmd-entrypoint-example "Custom message"
Custom message