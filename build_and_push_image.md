```
- docker buildx build --platform linux/amd64 -t gcr.io/<project-id>/<name-image>:v0.1.0 .

- docker push gcr.io/<project-id>/<name-image>:v0.1.0

- docker image ls

- docker tag gcr.io/<project-id>/<name-image>:v0.1.0 gcr.io/<project-id>/<another-name-image>:v0.1.0

- docker rmi <image-id>
```
