import hashlib
import time

def minerar_bloco(dados, target):
    """
    Função que tenta encontrar um nonce tal que o hash SHA-256 do
    dado concatenado com o nonce seja menor que o target numérico.
    """
    nonce = 0  # Começamos o nonce em 0
    print("\nMinerando bloco com os dados:", dados)
    print(f"Target em hexadecimal (64 caracteres): {target:064x}")
    
    inicio = time.time()

    while True:
        # Concatenamos os dados com o nonce para formar a base do hash
        texto = dados + str(nonce)
        hash_bytes = hashlib.sha256(texto.encode('utf-8')).digest()
        hash_int = int.from_bytes(hash_bytes, byteorder='big')
        hash_hex = hash_bytes.hex()

        # Verificamos se o hash está dentro do alvo (target)
        if hash_int < target:
            tempo_gasto = time.time() - inicio
            print(f"✅ Nonce encontrado: {nonce}")
            print(f"✅ Hash válido: {hash_hex}")
            print(f"⏱ Tempo gasto: {tempo_gasto:.4f} segundos")
            return nonce, hash_hex
        
        # Se não for válido, tentamos o próximo nonce
        nonce += 1

# --- DEFINIÇÃO DA ESTRUTURA DO BLOCO ---

class Bloco:
    def __init__(self, indice, dados, hash_anterior):
        """
        Construtor de um bloco da blockchain.
        
        - indice: posição do bloco na cadeia.
        - dados: conteúdo (ex: transações).
        - hash_anterior: hash do bloco anterior (encadeamento).
        """
        self.indice = indice
        self.dados = dados
        self.timestamp = time.time()
        self.hash_anterior = hash_anterior
        self.nonce = None
        self.hash = None

    def minerar(self, target):
        """
        Gera o hash válido para este bloco baseado nos seus dados e no hash anterior.
        """
        # Criamos o texto base do bloco: índice, timestamp, dados, hash anterior
        texto_bloco = f"{self.indice}{self.timestamp}{self.dados}{self.hash_anterior}"
        
        # Usamos a função de mineração já definida
        self.nonce, self.hash = minerar_bloco(texto_bloco, target)

# --- PARÂMETROS DE DIFICULDADE ---

# Target em hexadecimal: quanto mais zeros à esquerda, mais difícil
target_hex = "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
target_int = int(target_hex, 16)

# --- CRIANDO A BLOCKCHAIN ---

blockchain = []  # Lista que conterá todos os blocos

# Criamos o bloco gênesis manualmente (sem hash anterior)
bloco_genesis = Bloco(0, "Bloco Gênesis - início da cadeia", "0" * 64)
bloco_genesis.minerar(target_int)
blockchain.append(bloco_genesis)

# Adicionamos mais 2 blocos na sequência, sempre usando o hash do bloco anterior
bloco_1 = Bloco(1, "MelhoreNegocio envia 10 moedas para ChatGPT", bloco_genesis.hash)
bloco_1.minerar(target_int)
blockchain.append(bloco_1)

bloco_2 = Bloco(2, "ChatGPT envia 5 moedas para MelhoreNegocio", bloco_1.hash)
bloco_2.minerar(target_int)
blockchain.append(bloco_2)

# --- EXIBINDO A BLOCKCHAIN COMPLETA ---

print("\n📦📦📦 Blockchain completa:")
for bloco in blockchain:
    print("\n--- Bloco", bloco.indice, "---")
    print("Timestamp:", time.ctime(bloco.timestamp))
    print("Dados:", bloco.dados)
    print("Hash anterior:", bloco.hash_anterior)
    print("Nonce:", bloco.nonce)
    print("Hash:", bloco.hash)
