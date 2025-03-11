import click

from k8s_docker_cli.docker import build, push, registry
from k8s_docker_cli.kubernetes import apply, delete, namespace
from k8s_docker_cli.kubeconfig import manage


@click.group()
@click.version_option()
def main():
    """CLI to operate with Docker, Kubernetes and manage Kubeconfig"""
    pass


### DOCKER PART ###
@main.group()
def docker():
    """Docker images commands"""
    pass


@docker.command("build")
@click.argument("path", type=click.Path(exists=True))
@click.option("--tag", "-t", required=True, help="Tag of Docker image")
@click.option("--dockerfile", "-f", default="Dockerfile", help="Path/to/Dockerfile")
def docker_build(path, tag, dockerfile):
    """Builds docker image"""
    build.build_image(path, tag, dockerfile)


@docker.command("push")
@click.argument("image", required=True)
@click.option("--registry", "-r", help="Registry où pousser l'image")
def docker_push(image, registry):
    """Push image to registry"""
    push.push_image(image, registry)


@docker.command("registry-login")
@click.argument("registry", reguired=True)
@click.option("--username", "-u", required=True, help="User name")
@click.option("--password", "-p", required=True, help="Password")
def docker_registry_login(registry, username, password):
    """Connect to a Docker registry"""
    registry.login(registry, username, password)


### KUBERNETES PART ###


@main.group()
def kubernetes():
    """Commands to operate with kubernetes"""
    pass


@kubernetes.command("apply")
@click.argeument("file", type=click.Path(exists=True))
@click.option("--namespace", "-n", help="Target namespace")
def kubernetes_apply(file, namespace):
    """Apply manifest"""
    apply.apply_manifest(file, namespace)


@kubernetes.command("delete")
@click.argument("file", type=click.Path(exists=True))
@click.option("--namespace", "-n", help="Target namespace")
def kubernetes_delete(file, namespace):
    """Delete every resource used by manifests"""
    delete.delete_manifest(file, namespace)


@kubernetes.command("create-namespace")
@click.argument("name", required=True)
def kubernetes_create_namespace(name):
    """Create namespace"""
    namespace.create_namespace(name)


@kubernetes.command("delete-namespace")
@click.argument("name", required=True)
def kubernetes_delete_namespace(name):
    """Delete namespace"""
    namespace.delete_namespace(name)


### KUBECONFIG PART ###
@main.group()
def kubeconfig():
    """Commands to gerate kubeconfig"""
    pass


@kubeconfig.command("use-context")
@click.argument("context", required=True)
def kubeconfig_use_context(context):
    """Changing context for Kubeconfig"""
    manage.use_context(context)


@kubeconfig.command("list-contexts")
def kubeconfig_list_contexts():
    """Get a contexts list"""
    manage.list_contexts()


@kubeconfig.command("add-config")
@click.argument("config_file", type=click.Path(exists=True))
@click.option(
    "--merge/--replace", default=True, help="Merge or replace current kubeconfig_file"
)
def kubeconfig_add_config(config_file, merge):
    """Adding a new kubeconfig"""
    manage.add_config(config_file, merge)


if __name__ == "__main__":
    main()
