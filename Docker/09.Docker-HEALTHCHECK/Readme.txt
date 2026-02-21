interval - 30s
timeout - 30s
start-period - 0s
start-interval - 0s  --> During the start-period, the health check will run every x seconds. This allows for quicker health status updates during startup.
retries - 3
Staus -> starting, healthy, unhealthy
Not use inherited healthcheck
- HEALTHCHECK NONE

docker build -t nginx:hc .
docker inspect nginx:hc --format='{{json .Config.Healthcheck}}' | jq
docker run --name hc-1 -p 8080:80 -d nginx:hc
docker ps --> Look for healthy
docker inspect hc-1 --format='{{json .State.Health}}' | jq
