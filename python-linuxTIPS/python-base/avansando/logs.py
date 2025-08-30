#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from logging import handlers

# Handler eh a classe responsavel pelo destino
# de onde o log sera impresso


# Boilerplate
# TODO: tranformar em funçao
# TODO: usar lib (loguru)
# o log PODE SER CUSTOMIZADO:
    # instancia de log
log = logging.Logger("Mr.Robot", logging.DEBUG)

    # level do log
# console_handler = logging.StreamHandler() #handler para console
# console_handler.setLevel(logging.DEBUG) # setando level do handler
# ou
file_handler = handlers.RotatingFileHandler( #handler para arquivo
    "meulog.log",
    maxBytes=100, # 10 ** 6
    backupCount=10,
)
file_handler.setLevel(logging.DEBUG)

    # formatar o log
format_log = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
     ' line:%(lineno)d file:%(filename)s: %(message)s'
) #formatando como a mensagem aparece
#console_handler.setFormatter(format_log) #objeto dentro do handler
file_handler.setFormatter(format_log) #objeto dentro do handler

    # destino do log
# log.addHandler(console_handler) #adiciona o handler ao log
log.addHandler(file_handler) #adiciona o handler ao log



# logging.debug("Mensagem pro dev.")
# logging.info("Mensagem geral para usuarios")
# logging.warning("Aviso que nao causa erro.")
# logging.error("Erro que afeta uma unica execucao,ou usuario")
# logging.critical("Erro geral , ex: banco de dados sumiu")

log.debug("Mensagem pro dev.")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro.")
log.error("Erro que afeta uma unica execucao,ou usuario")
log.critical("Erro geral , ex: banco de dados sumiu")

logging.critical("DEU PROBLEMA GERAL!")

"""
try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))
    print(f"[ERRO] Deu erro {str(e)}")
    # o print fala com o stdout
    # existe outra interface, chamada stderr
"""


try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))