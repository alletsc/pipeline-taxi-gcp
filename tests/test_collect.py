import pytest

from taxi_gcp.core import collect
from tests.constants import PATH_DATA


@pytest.mark.unit
@pytest.mark.high
def test_collect_function():
    """Testa se a função collect retorna arquivos de um diretório e retorna o caminho base."""
    collected_files, path_data = collect(PATH_DATA)
    assert len(collected_files) == 2  # 2 arquivos na pasta tests/assets
    assert path_data == PATH_DATA  # O caminho base é o mesmo que o fornecido
    assert all(
        [f.startswith(PATH_DATA) for f in collected_files]
    )  # os arquivos estão na pasta tests/assets
    assert all([f.endswith(".csv") for f in collected_files])  # os arquivos são CSV
    assert collect("tests/assets/empty") == (
        [],
        "tests/assets/empty",
    )  # teste para lidar com diretorios vazios
