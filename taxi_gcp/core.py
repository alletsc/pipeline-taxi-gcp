""" Core module for taxi_gcp package """

import os

from taxi_gcp.utils.logger import get_logger

log = get_logger()


def collect(path_data):
    """Coleta os arquivos de path_data e retorna uma tupla:
    O primeiro elemento é uma lista dos caminhos completos dos arquivos
    coletados, e o segundo é o caminho base fornecido."""
    try:
        # Garante que apenas arquivos (não diretórios) sejam listados
        collected_files = [
            os.path.join(path_data, f)
            for f in os.listdir(path_data)
            if os.path.isfile(os.path.join(path_data, f))
        ]
        log.info(f"Arquivos coletados: {collected_files}")
        # Retorna tanto os arquivos coletados quanto o caminho base
        return collected_files, path_data
    except FileNotFoundError as e:
        log.error(f"Erro ao coletar arquivos em {path_data}: {e}")
        raise e
