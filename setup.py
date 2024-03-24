import os

from setuptools import find_packages, setup


def read(*paths):
    """Lê o contexto de um arquivo de texto de forma segura."""
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()

def read_requirements(path):
    """Lê as dependências do projeto a partir de um arquivo .txt."""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', '-'))
    ]


setup(
    name='taxi_gcp',
    version='0.1.0',
    description='Pipeline for taxi data on GCP',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author='Stella Costa',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "taxi_gcp=taxi_gcp.__main__:main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements-test.txt"),
        "dev": read_requirements("requirements-dev.txt")
    }
)
