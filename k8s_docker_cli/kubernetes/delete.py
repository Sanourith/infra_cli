import subprocess
import os
import yaml
import click


def delete_manifest(file_path, namespace=None):
    """Delete a manifest application

    Args:
        file_path (str): path/to/manifest
        namespace (str, optional): Target namespace. Defaults to None.
    """
    if not os.path.exists(file_path):
        click.echo(f"Error: file {file_path} doesn't exists.")
        return False

    try:
        with open(file_path, "r") as file:
            yaml.safe_load(file)
    except yaml.YAMLError as e:
        click.echo(f"Error: file {file_path} isn't a YAML file : {e}")
        return False

    cmd = ["kubectl", "delete", "-f", file_path]

    if namespace:
        cmd.extend(["-n", namespace])

    click.echo(
        f"Delete manifest {file_path}"
        + (f" into namespace {namespace}" if namespace else "")
        + "..."
    )

    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        click.echo(result.stdout)
        click.echo(f"Manifest {file_path} deleted successfully")
        return True
    except subprocess.CalledProcessError as e:
        click.echo(f"Error calling manifest : {e}", err=True)
        click.echo(e.stderr, err=True)
        return False
