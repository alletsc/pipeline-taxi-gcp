MARKER = """
integration: marca para testes de integração
unit: marca para testes de unidade
high: marca para testes de alta prioridade
low: marca para testes de baixa prioridade
medium: marca para testes de média prioridade
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)
