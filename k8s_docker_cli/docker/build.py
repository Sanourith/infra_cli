import subprocess
import click
import os


def build_image(path, tag, dockerfile="Dockerfile"):
    """Build a Docker image

    Args:
        path (str): path/to/dockerfile
        tag (str): image tag
        dockerfile (str, optional): Dockerfile's name. Defaults to "Dockerfile".
    """
    dockerfile_path = os.path.join(path, dockerfile)
    if not os.path.exists(dockerfile_path):
        click.echo(f"Error: Dockerfile {dockerfile_path} doesn't exists.")
        return False

    click.echo(f"Building image {tag} from {dockerfile_path}")

    try:
        cmd = ["docker", "build", "-t", tag, "-f", dockerfile_path, path]
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        click.echo(result.stdout)
        click.echo(f"Image {tag} built successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error building image : {e}", err=True)
        click.echo(f"e.stderr", err=True)
        return False
