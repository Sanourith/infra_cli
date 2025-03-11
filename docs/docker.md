# Docker images management

This sections give information about docker images management with k8s-docker-cli.

## Build a Docker image

"Build" command permits to build a docker image from a Dockerfile.
```bash
k8s-docker docker build <PATH> -t <TAG> [-f <DOCKERFILE>]
```

### Arguments

* <PATH> : Link to directory with Dockerfile
* -t, --tag <TAG> : tag_name for images (required)
* -f, --dockerfile <DOCKERFILE> : Dockerfile's name (default = Dockerfile)

### eg

```bash
# Build an image from Dockerfile
k8s-docker docker build . -t mon-app:1.0.0

# Build a spec image with a specific Dockerfile
k8s-docker docker build . -t mon-app:1.0.0 -f Dockerfile.prod
``` 

## Push img to registry
"Push" command permits to push image on a registry.

```bash
k8s-docker docker push <IMAGE> [-r <REGISTRY>]
```

### Arguments
* <IMAGE> Image name
* -r, --registry <REGISTRY> adresse for registry (optional)
