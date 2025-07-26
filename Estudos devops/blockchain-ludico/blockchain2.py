import hashlib
import time

def minerar_bloco(dados, target):
    """
    Função que tenta encontrar um nonce tal que o hash SHA-256 do
    dado concatenado com o nonce seja menor que o target numérico.
    
    Parâmetros:
    dados (str): O conteúdo do bloco que será minerado.
    target (int): O valor alvo máximo que o hash convertido para inteiro
                  deve ser menor para que o bloco seja válido.
    
    Retorna:
    nonce (int): O nonce que gera o hash válido.
    hash_hex (str): O hash válido em hexadecimal.
    tempo_gasto (float): Tempo que levou para minerar em segundos.
    """

    nonce = 0  # Começamos o nonce em 0 e iremos incrementando até achar hash válido

    print(f"Target numérico para mineração: {target}")
    print(f"Target em hexadecimal (64 caracteres): {target:064x}")
    print("Iniciando mineração...")

    inicio = time.time()

    while True:
        # Concatenamos os dados com o nonce atual, transformando nonce em string
        texto = dados + str(nonce)

        # Calculamos o hash SHA-256 desse texto
        hash_bytes = hashlib.sha256(texto.encode('utf-8')).digest()

        # Convertendo o hash em inteiro para comparação numérica
        hash_int = int.from_bytes(hash_bytes, byteorder='big')

        # Convertendo o hash em hexadecimal para exibir
        hash_hex = hash_bytes.hex()

        # Verificamos se o hash gerado é menor que o target numérico
        if hash_int < target:
            # Encontramos um nonce válido!
            fim = time.time()
            tempo_gasto = fim - inicio

            print(f"Nonce encontrado: {nonce}")
            print(f"Hash válido: {hash_hex}")
            print(f"Valor numérico do hash: {hash_int}")
            print(f"Tempo gasto: {tempo_gasto:.4f} segundos")
            return nonce, hash_hex, tempo_gasto
        
        # Caso não tenha sido válido, incrementamos o nonce e tentamos de novo
        nonce += 1

# --- Exemplo de uso ---

# Definimos os dados que estarão no bloco (pode ser qualquer string)
dados_do_bloco = "MelhoreNegocio envia 10 moedas para ChatGPT"

# Definimos o target numérico que define a dificuldade
# Quanto menor o target, mais difícil será achar o hash válido
# Aqui colocamos um valor alto para facilitar a mineração neste exemplo
# Por exemplo, vamos exigir que a hash seja menor que:
# 0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF (20 bits zeros iniciais)
target_hex = "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
target_int = int(target_hex, 16)

# Executamos a mineração
minerar_bloco(dados_do_bloco, target_int)
