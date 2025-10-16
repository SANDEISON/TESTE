# Classe FilaCircular
class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.quant = 0

    def enqueue(self, valor):
        if self.quant == self.tamanho:
            print("Fila cheia!")
            return
        self.fila[self.fim] = valor
        self.fim = (self.fim + 1) % self.tamanho
        self.quant += 1
        print(f"Enfileirado: {valor} | Fila atual: {self.fila}")

    def dequeue(self):
        if self.quant == 0:
            print("Fila vazia!")
            return
        valor = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.tamanho
        self.quant -= 1
        print(f"Removido: {valor} | Fila atual: {self.fila}")
        return valor


# =============================
# 🚀 TESTE DA FILA CIRCULAR
# =============================

# Cria uma fila circular com tamanho 3
fila = FilaCircular(3)

# Inserindo elementos
fila.enqueue("A")
fila.enqueue("B")
fila.enqueue("C")

# Tentando inserir mais um (fila cheia)
fila.enqueue("D")

# Removendo um elemento
fila.dequeue()

# Inserindo outro (agora deve usar o espaço liberado)
fila.enqueue("E")

# Removendo todos
fila.dequeue()
fila.dequeue()
fila.dequeue()

# Tentando remover com a fila vazia
fila.dequeue()
