# aula 24 - Linux Tips

# tratamentos de erros com Excessões

# CONTEUDO PRATICO NO ARQUIVO errors.py
# tambem arquivo names.txt


# Existem duas abordagens para resolver erros:
# PRIMEIRA: LBYL => Look Before You Leap : Olhe antes de atravessar a rua, ou de pular
# OBS: Estas OPERAÇOES de IO(input/output)
# podem demorar. Exemplo, usar(if,else) para verificar errors.
# ESTA OPÇAO causa o (Race Condition) , corrida de leitura entre arquivos, por exemplo doi programas que acessao o mesmo arquivo.


# ===>ESTA ABORDAGEM para errors EH A MELHOR!<=====
# SEGUNDA: EAFP => Easy to Ask Forgiveness than permission : É mais fácil pedir perdão do que permissão.

# usa-se o try , except, else, finally

# OBS: tratamento de erro tem que ser sempre ESPECIFICO!!!

# o raise, força o erro para acontecer.
