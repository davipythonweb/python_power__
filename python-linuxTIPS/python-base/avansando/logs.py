#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# Handler eh a classe responsavel pelo destino
# de onde o log sera impresso

# PODE SER CUSTOMIZADO:
    # nova instancia
log = logging.Logger("__name__", logging.DEBUG)
    # level do log
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG) 
    # formatar o log
format_log = logging.Formatter(
    '%(asctime)s %(names)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
    # destino do log



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