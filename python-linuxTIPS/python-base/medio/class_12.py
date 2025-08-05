# aula 12

# tipos de dados = textos

# str , plural = strings -> varios caracteres
# exemplo para saber quantos metodos há: len(dir(str)) = 81
# É utilizado a TABELA ASCII para converter os dados str
# existe outra tabela chamada : unicode , para simbulos e pictograph
# atualmente exsite a tabela : utf8 que tem 8bits

# unicode = 🐍 = U+1F40D

# serializaçao
# converte o emotion para hex
# ENCODE:  emotion = snake.encode("utf-8") = b'\xf0\x9f\x90\x8d'

# decodifica o emotion que estava em hexadecimal para utf-8
# DECODE:  emotion.decode() = '🐍'