# aula 12

# tipos de dados = textos

# str , plural = strings -> varios caracteres
# exemplo para saber quantos metodos há: len(dir(str)) = 81 metodos
# É utilizado a TABELA ASCII para converter os dados str
# existe outra tabela chamada : unicode , para simbulos e pictograph
# atualmente exsite a tabela : utf8 que tem 8bits

# unicode = 🐍 = U+1F40D

# serializaçao
# converte o emotion para hex
# ENCODE:  emotion = snake.encode("utf-8") = b'\xf0\x9f\x90\x8d'

# decodifica o emotion que estava em hexadecimal para utf-8
# DECODE:  emotion.decode() = '🐍'

# tranformando texto em bytes
# exemplo: nome = "Davi"

# transformando em binario
# exemplo: bytes(nome, "utf-8") = b'Davi'

# atribuindo o binario a uma lista para visualizar os bytes
# exemplo: list(bytes(nome, "utf-8")) = [68, 97, 118, 105]

# Sliceable (ser fatiado)
# exemplo: nome[0] = 'D'
# exemplo: nome[0:4] = 'Davi'