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


### eg
```bash
# Push an image to Docker Hub (if logged in)
k8s-docker docker push my-app:1.0.0

# Push an image to a specific registry
k8s-docker docker push my-app:1.0.0 -r registry.example.com
```

## Logging into a Docker Registry

The registry-login command allows you to log in to a Docker registry.
```bash
k8s-docker docker registry-login <REGISTRY> -u <USERNAME> -p <PASSWORD>
```

### Arguments

* <REGISTRY>: Address of the registry.
* -u, --username <USERNAME>: Username.
* -p, --password <PASSWORD>: Password

### eg 
```bash
# Log in to Docker Hub
k8s-docker docker registry-login docker.io -u myusername -p mypassword

# Log in to a private registry
k8s-docker docker registry-login registry.example.com -u myusername -p mypassword
```

## Best Practices

### Credential security
```bash
# Using environment variables
export REGISTRY_PASSWORD="mysecretpassword"
k8s-docker docker registry-login registry.example.com -u myusername -p $REGISTRY_PASSWORD
```

### Image Tagging
It is recommended to use a consistent tagging system:

* Use semantic versioning (1.0.0, 1.0.1, etc.) for stable releases.
* Use commit-based or branch-based tags for development versions.

## Multi-Architecture Support

If you need to build images for multiple architectures (x86_64, ARM, etc.), you can use Docker BuildX:

```bash
# Initialize BuildX (only required once)
docker buildx create --name mybuilder --use

# Then build using k8s-docker-cli
k8s-docker docker build . -t my-app:1.0.0 -f Dockerfile.multi-arch
```

## Troubleshooting
###Common Issues


### Authentication Error
Verify your credentials.
#### Ensure your user has the necessary permissions on the registry.
Build Error
#### Check that all dependencies are available.
Ensure the build context (path) is correct.
#### Image Too Large
Use lighter base images.
Implement multi-stage builds in your Dockerfile.
Clean up cache and temporary files in your Docker layers.