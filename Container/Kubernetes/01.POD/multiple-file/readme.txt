?? Define multiple object in sane file
- Add three dashes between each object.
- Useful when installing once.
- Not much useful when updating which target on one object. Which might try to apply all object in the same file.

% kubectl apply -f nginx-multi.yaml
or)
% kubectl apply -f .

% kubectl create -f nginx-multi.yaml
# Says object already exist