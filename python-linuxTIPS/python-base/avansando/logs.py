#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    1 / 0
except ZeroDivisionError as e:
    print(f"[ERRO] Deu erro {str(e)}")