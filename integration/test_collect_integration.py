import subprocess

import pytest

from integration.constants_integration import PATH_DATA


@pytest.mark.integration
@pytest.mark.medium
def test_collect_command_integration():
    """Testa se o comando collect está funcionando corretamente."""
    try:
        # Executa o comando e captura a saída
        output_bytes = subprocess.check_output(["taxi_gcp", "collect", PATH_DATA])
        # Decodifica a saída para uma string e divide por linha
        output_decoded = output_bytes.decode("utf-8").split("\n")
        # Concatena as linhas decodificadas para facilitar a verificação de presença
        filenames = "\n".join(output_decoded)
        # Verifica se os arquivos esperados estão presentes na saída
        assert "drives.csv" in filenames
        assert "races.csv" in filenames
    except subprocess.CalledProcessError as error:
        # Se o comando retornar um código de erro, imprime a saída para debug
        print(error.output.decode("utf-8"))
        raise error
