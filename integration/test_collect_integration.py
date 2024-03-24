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
        assert "drives.csv" in output_decoded[1]
        assert "races.csv" in output_decoded[2]
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando collect: {e.output.decode('utf-8')}")
        raise
