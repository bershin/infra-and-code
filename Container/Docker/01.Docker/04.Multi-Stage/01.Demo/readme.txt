?? What is distroless image?
Minimal Docker images that contains only the necessary runtime dependencies of applications.
Unless traditional images that include an operating system, shell utilities and other binaries, distroless images exclude these components, resulting in a more smaller and secured image.

?? Advantages of distroless image?
- Enhanced Security:Fewer component means fewer vulnerability & smaller attack surface.
- Reduced Image size: Faster image pull & reduced storage.
- Improved Performance: Smaller size means quick container startup & lower resource consumption.
- Simplified Complainance & Autitability:  Easy to audit and verify with fewer components.

?? Challenges of distroless image?
- No Debuggin Tools: Without shell utilities or debugging tools troubleshooting issues inside a distroless container is challenging.
- Dependency management: Managing dependencies is more complex, Since no OS utilities as you need to ensure all required libraries and binaries are included in the build process.
- Increasing Build Complexity: Craeting distroless images often involves more complex Dockerfile and build processes.
- Learning Curve: The knowledge from traditional images is not immediately applicable due to the lack of familiar tools and a different debugging workflow.


?? Demo: multistage with express get helloworld with '/'
- Use distro to build -> fail
    - % docker build -t multistage-example .
- Use multistage to do same.
    % docker build -t multistage-example .
    % docker rum --rm -d -p 3001:3000  multistage-example 
    % curl http://localhost:3001
    % docker exec -it <container> sh --> fail






