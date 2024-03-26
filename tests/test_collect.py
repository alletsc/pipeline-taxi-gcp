import pytest

from taxi_gcp.core import collect
from tests.constants import PATH_DATA


@pytest.mark.unit
@pytest.mark.high
def test_positive_has_2_files():
    """Testa se a função collect retorna 2 arquivos do PATH_DATA."""
    collected_files, path_data = collect(PATH_DATA)
    assert len(collected_files) == 2  # 2 arquivos na pasta tests/assets


@pytest.mark.unit
@pytest.mark.high
def test_positive_path_data_and_files():
    """Testa se o caminho base é o mesmo que o fornecido."""
    collected_files, path_data = collect(PATH_DATA)
    assert path_data == PATH_DATA  # O caminho base é o mesmo que o fornecido


@pytest.mark.unit
@pytest.mark.high
def test_positive_files_are_in_path_data():
    """Testa se os arquivos coletados estão na pasta PATH_DATA"""
    collected_files, path_data = collect(PATH_DATA)
    assert all(
        [f.startswith(PATH_DATA) for f in collected_files]
    )  # os arquivos estão na pasta tests/assets


@pytest.mark.unit
@pytest.mark.high
def test_positive_files_are_csv():
    """Testa se os arquivos são .csv"""
    collected_files, path_data = collect(PATH_DATA)
    assert all([f.endswith(".csv") for f in collected_files])  # os arquivos são CSV
