?? What is docker images?
Images are self-contained, read-only template(blueprint) that "encapsulate everything" needed to run your application.
A docker image is like a snapshot of your application and its complete runtime environment, frozen in time and ready to be brought to life as a container
- The base layer: Minimum linux distro(alphine) or full fledged(ubuntu)
- Runtime Environment: Software for the application (Python/NodeJS)
- Libraries & dependencies: All external code your app relies on like "express"
- Application code: Your own Source code / Compiled code
- Configuration: Settings for application and its environment.(option)

Image can be sourced from multiple location:
- Docker hub: Official docker repository contains various images.
- Private registry: Private registry for organizations(properitory software/ Sensitive image) & granular access for authorized users.
- Build your own image: Created using docker file.

?? Benefits of container registry?
- Collaboration: Share your image with wider community(others).
- Versioning: Easy rollback & update(application evolves)
- Security: Private registry for sensitive image.
- Automation: Automate image building & deployment through CI/CD pipeline

?? Consider when selecting container registries.
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
    - Open-Source - Free to use, but requires infrastructure and maintenance investment.

?? Relation between image tag & id?
Am image is uniquely defined by its image ID. 
- Multiple tags are simple human redable pointers or aliases that can refer(point) to the exact same image.

?? Why pin the version to the software you are working with?
- Latest tag is a moving pointer that changes whenever a new image is published.
- Gives high degree of stability.
- Pinning to a spefic version ensure that build are reproducable and prevent the application from breaking unexpectedly due to unvetted changes in the base image.
- update the version regularly and pin it, when fixing vulnerabilty.

?? Login into docker hub, why is it important?
$ docker login
<create access token as password>
- login required to push public/private image and pull private image.

# Pull all images with their tag to local from docker hub
docker search hello-world (will not show tags)
docker pull hello-world (will pull the latest)
docker pull --all-tags hello-world

# Build a hello world image using ubuntu and tag and push to docker hub. Then delete the repo.
% vi Dockefile
% docker build -t simple_hello_world:latest .
% docker tag simple_hello_world:latest 230882/simple_hello_world:v0.0.1
% docker push 230882/simple_hello_world:v0.0.1
# Delete the reposioty in docker hub

?? Docker image vs Docker container
- An image is a read-only static blueprint containing the application and its environment.
- A container is a live, running and writable instance created from the image.