#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# PODE SER CUSTOMIZADO:
    # level do erro
    # formatar o erro (É preciso criar uma nova instancia)
    # destino do erro

logging.debug("Mensagem pro dev.")
logging.info("Mensagem geral para usuarios")
logging.warning("Aviso que nao causa erro.")
logging.error("Erro que afeta uma unica execucao,ou usuario")
logging.critical("Erro geral , ex: banco de dados sumiu")

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