#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

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