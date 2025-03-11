from setuptools import setup, find_packages

setup(
    name="k8s-docker-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "docker>=5.0.0",
        "kubernetes>=12.0.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "k8s-docker=k8s_docker_cli.cli:main",
        ],
    },
    author="Sanou",
    author_email="ma-mail@example.com"
    description="CLI to use Docker, Kubernetes & manage Kubeconfig"
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sanourith/infra_cli"
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
