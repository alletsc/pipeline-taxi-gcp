import logging
import os
from logging import handlers

# BOILERPLATE CODE
LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
# Cria uma instância do logger com o nome específico.
log = logging.getLogger(name="taxi_gcp")
# Define o formato das mensagens de log.
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - "
    "l:%(lineno)d - f:%(filename)s: %(message)s"
)


def get_logger(logfile="taxi_gcp.log"):
    """Retorna o logger configurado para o pacote taxi_gcp"""
    log.setLevel(LOG_LEVEL)
    fh = handlers.RotatingFileHandler(
        filename=logfile,
        maxBytes=10**6,  # 1MB
        backupCount=10,  # Mantém backups dos últimos 10 arquivos de log.
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    # Verifica se o handler já foi adicionado ao logger.
    if not any(
        isinstance(handler, handlers.RotatingFileHandler)
        and handler.baseFilename == fh.baseFilename
        for handler in log.handlers
    ):
        log.addHandler(fh)
    return log
