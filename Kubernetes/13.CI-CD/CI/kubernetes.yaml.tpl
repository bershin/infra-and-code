apiVersion: apps/v1
kind: Deployment
metadata:
  name: app1-deployment
spec:
  selector:
    matchLabels:
      app: app1
  template:
    metadata:
      labels:
        app: app1
    spec:
      containers:
      - name: app1
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/bjohn-ar-us-central/test-ar:COMMIT_SHA
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: app1-service
spec:
  type: LoadBalancer
  selector:
    app: app1
  ports:
  - port: 80
    targetPort: 80
---