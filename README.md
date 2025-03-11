# WIP - ultra package

# K8s-docker-cli

A CLI to manipulate Docker images, Kubernetes manifests & kubeconfig files.

## Installation

```bash
# from Github
pip install git+https://github.com/username/k8s-docker-cli.git

# locally
git clone https://github.com/username/k8s-docker-cli.git
cd k8s-docker-cli
pip install -e .
```

## Prerequisites

* Python 3.7+
* Docker installation
* Kubectl installation

## Usage

After installation, you can use the CLI with k8s-docker :
```bash
# General help
k8s-docker --help

# Display help for modules
k8s-docker docker --help
k8s-docker kubernetes --help
k8s-docker kubeconfig --help
``` 

## Docker images management

```bash
# Build a Docker image
k8s-docker docker build . -t mon-image:latest

# Push an image into registry
k8s-docker docker push mon-image:latest -r registry.example.com

# Connect to registry
k8s-docker docker registry-login registry.example.com -u username -p password
``` 

## Kubernetes manifests management

```bash 
# Apply a Kubernetes manifest
k8s-docker kubernetes apply manifest.yaml -n mon-namespace

# Delete a Kubernetes manifest
k8s-docker kubernetes delete manifest.yaml -n mon-namespace

# Create namespace
k8s-docker kubernetes create-namespace mon-namespace

# Delete namespace
k8s-docker kubernetes delete-namespace mon-namespace
``` 

## Kubeconfig management

```bash
# Get a contexts list
k8s-docker kubeconfig list-contexts

# Changing context
k8s-docker kubeconfig use-context mon-contexte

# Merging kubeconfig
k8s-docker kubeconfig add-config nouveau-config.yaml --merge

# Replace existing kubeconfig
k8s-docker kubeconfig add-config nouveau-config.yaml --replace
```

# Documentation

To get a better documentation, you might check docs/ directory :
* General usage guide
* Docker images management
* Kubernetes manifest management
* Kubeconfig management

## Contributors

All contributors are welcome, my project is a schoolar-type to try something new with python.

## Licence
There is no licence, everything a sharing free.
