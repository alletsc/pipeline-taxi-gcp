import os

import pkg_resources
import rich_click as click
from rich import print  # noqa
from rich.console import Console
from rich.table import Table

from taxi_gcp import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.USE_RICH_PROGRESS = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVAR_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("taxi_gcp").version)
def main():
    """Taxi-GCP: pacote para integração com o GCP"""


@main.command()
@click.argument("path_data", type=click.Path(exists=True))
def collect(path_data):
    """Coleta arquivos de um diretório e retorna uma tupla com os caminhos.
    - Valida se o diretório existe.
    - Coleta apenas arquivos (não diretórios).
    - Retorna uma tupla com os caminhos dos arquivos e o caminho.
    """

    # Adicicionando barra de progresso com rich
    table = Table(title="Arquivos coletados")
    headers = ["Caminho", "Nome do arquivo", "Tamanho (KB)"]
    for header in headers:
        table.add_column(header, style="magenta")

    result = core.collect(path_data)
    for file_ in result[0]:
        size_in_kb = os.path.getsize(file_) / 1024
        table.add_row(file_, file_.split("/")[-1], str(round(size_in_kb, 2)))

    Console().print(table)
