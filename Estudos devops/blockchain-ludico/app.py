import hashlib  # biblioteca para gerar hashes (ex: SHA-256)
import time     # para medir o tempo de mineração

"""nonce= NUMERO ONDE INICIA A PROCURAR
dificuldade= NUMERO DE ZEROS
dados=A MENSSAGEM ENVIADA
hash=NUMERO EXADECIMAL GERADO POR SHA-256"""

# Função que simula a mineração (prova de trabalho)
def minerar_bloco(dados, dificuldade):
    nonce = 0  # número que será alterado até encontrar o hash válido(determina onde o codigo começa a procurar.)
    prefixo = '0' * dificuldade  # exemplo: '0000' se dificuldade for 4(nivel de dificuldade de satisfaçao)

    print(f"Iniciando a mineração com dificuldade {dificuldade}...")
    inicio = time.time()

    while True:
        # Monta o texto do bloco com os dados + nonce
        texto_bloco = dados + str(nonce)

        # Calcula o hash SHA-256 desse texto
        hash_resultado = hashlib.sha256(texto_bloco.encode()).hexdigest()

        # Verifica se o hash começa com o número certo de zeros
        if hash_resultado.startswith(prefixo):
            fim = time.time()
            print(f"\n✅ Bloco minerado com sucesso!")
            print(f"Nonce encontrado: {nonce}")
            print(f"Hash válido: {hash_resultado}")
            print(f"Tempo: {fim - inicio:.2f} segundos")
            break

        # Se não for válido, tenta outro nonce
        nonce += 1

# Exemplo de uso
dados_do_bloco = "Transação de Alice para Bob: 10 moedas"
dificuldade = 1  # Aumente para 5 ou 6 para ver ficar mais difícil ( simboliza os zeros)

minerar_bloco(dados_do_bloco, dificuldade)
