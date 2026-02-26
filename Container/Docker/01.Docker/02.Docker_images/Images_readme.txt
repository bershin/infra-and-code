# What is docker images?
Images are self-contained, read-only template(blueprint) that encapsulate everything needed to run your application.
A docker image is like a snapshot of your application and its complete runtime environment, frozen in time and ready to be brought to life as a container
- The base layer: Minimum linux distro(alphine) or full fledged(ubuntu)
- Runtime Environment: Software for the application (Python/NodeJS)
- Libraries & dependencies: All external code your app relies on like express
- Application code: Your own Source code / Compiled code
- Configuration: Settings for application and its environment.
Image can be sourced from multiple location:
- Docker hub: Official docker repository contains various images.
- Private registry: Private registry for organizations(properitory software/ Sensitive image) & granular access for authorized users.
- Build your own image: Created using docker file.

# Benefits of container registry?
- Collaboration: Share your image with wider community(others).
- Versioning: Easy rollback & update
- Security: Private registry for sensitive image.
- Automation: Automate image building & deployment through CI/CD pipeline

# Consider when selecting container registries.
- Hosting Type
    - public(opensource project)
    - private(properitory software/ Sensitive image) - Need authentication for pulling image even.
    - Self-hosted(offer flexibility, require infrastructure management)
    - Cloud-Hosted(convenient, scalable & integerate with cloud service)
- Security feature
    - Basic Authentication(Less sensitive project or public images)
    - Advanced(RBAC, Scanning, Signing) - Sensitive data, compliance requirment & secure deployment.
- Integeration
    - Limited - Standalone project / Simple workflow
    - Entensive(API, Webhook, CI/CD) - Enable automation, complex workflow & integeration with other tools.
- Cost model
    - Free Tier - Experimenation, small projects or public images.
    - Usage-Based - Flexible, but cost can scale with storage & bandwidth needs.
    - Fixed Subscription - Pedictable costs, but not be suitable for low usage.
    - Open-Source - 

# Relation between image tag & id?
Am image is uniquely defined by its image ID. Multiple tags are simple human redable pointers or aliases that can refer to the exact same image.

# Pull all images with their tag to local from docker hub
docker pull --all-tags hello-world

# Build a hello world image using ubuntu and tag and push to docker hub. Then delete the repo.
docker build -t simple_hello_world:latest .
docker tag simple_hello_world:latest 230882/simple_hello_world:v0.0.1
docker push 230882/simple_hello_world:v0.0.1
# Delete the reposioty in docker hub
