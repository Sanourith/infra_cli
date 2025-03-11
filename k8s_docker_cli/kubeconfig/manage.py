import subprocess
import click
import os
import yaml
import tempfile
import shutil


def use_context(context):
    """Change the active kubeconfig context.

    Args:
        context (str): Name of the context to use.
    """
    try:
        cmd = ["kubectl", "config", "use-context", context]
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        click.echo(result.stdout)
        click.echo(f"Context changed for {context}")
        return True
    except subprocess.CalledProcessError as e:
        click.echo(f"Error loading context {e}", err=True)
        click.echo(e.stderr, err=True)
        return False


def list_contexts():
    """Returns contexts list"""
    try:
        cmd = ["kubectl", "config", "get-contexts"]
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        click.echo(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        click.echo(f"Error loading contexts {e}")
        click.echo(e.stderr, err=True)
        return False


def add_config(config_file, merge=True):
    """Adds a new kubeconfig file

    Args:
        config_file (str): path/to/config_file
        merge (bool, optional): True = merge, False = replace. Defaults to True.
    """
    if not os.path.exists(config_file):
        click.echo(f"Error : file {config_file} doesn't exists", err=True)
        return False

    try:
        with open(config_file, "r") as file:
            yaml.safe_load(file)
    except yaml.YAMLError as e:
        click.echo(f"Error: file {config_file} isn't a YAML file.")
        return False

    if merge:
        try:
            kubeconfig_env = os.environ.get(
                "KUBECONFIG", os.path.expanduser("~/.kube/config")
            )
            cmd = ["kubectl", "config", "view", "--flatten"]

            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                result = subprocess.run(cmd, check=True, text=True, capture_output=True)
                tmp_file.write(result.stdout.encode())
                tmp_file.flush()

                env_vars = os.environ.copy()
                env_vars["KUBECONFIG"] = f"{tmp_file.name}:{config_file}"

                merge_cmd = ["kubectl", "config", "view", "--flatten"]
                result = subprocess.run(
                    merge_cmd, check=True, text=True, capture_output=True, env=env_vars
                )

                backup_path = os.path.expanduser("~/.kube/config.bkp")
                if os.path.exists(os.path.expanduser("~/.kube/config")):
                    shutil.copy2(os.path.expanduser("~/.kube/config"), backup_path)
                    click.echo(f"Saving existing kubeconfig in {backup_path}")

                with open(os.path.expanduser("~/.kube/config"), "w") as kube_config:
                    kube_config.write(result.stdout)

                click.echo("Kubeconfig merged successfully.")

            os.unlink(tmp_file.name)
            return True

        except subprocess.CalledProcessError as e:
            click.echo(f"Error merging kubeconfig : {e}", err=True)
            click.echo(e.stderr, err=True)
            return False

    else:
        try:
            if os.path.exists(os.path.expanduser("~/.kube/config")):
                backup_path = os.path.expanduser("~/.kube/config.bkp")
                shutil.copy2(os.path.expanduser("~/.kube/config"), backup_path)
                click.echo(f"Saving existing kubeconfig into {backup_path}")

            shutil.copy2(config_file, os.path.expanduser("~/.kube/config"))
            click.echo(f"Kubeconfig replaced successfully")
            return True
        except Exception as e:
            click.echo(f"Error replacing kubeconfig : {e}")
            return False
