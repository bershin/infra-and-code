?? Docker compose better than Docker
Docker compose is more robust for multi-container management for development workflow.

?? Why managing multi-container application only using Docker can be very challanging
- Manually starting multiple container and linking them is error-prone.
- Ensuring containers start in the correct order can be challenging.
- It is difficult to ensure consistency across environments leading to bug and integeration issues.
- Managing networks for inter-container communication and volumes for persistence storage across container restarts is no simple task.
- Managing configuration via environmental variable can be complex and require checking multiple places to get a consolidated view of the configuration.

?? When to use docker compose
- Local Development: Create consistent development environment easily.
- Testing & Staging environment: Replicate production environments for accurate testing.
- CI/CD Pipelines: Automate environment setup during build and deployment.(docker compose up -d;./test;docker compose down)
- Single host production deployments: Ideal for small-scale production setups.(k8s suitable for multihost deployment)

?? Difference between docker-compose Vs docker compose
docker compose is a plugin get installed when installing docker desktop.
Standalone docker compose is docker-compose.

?? Check docker compose version
% docker compose version