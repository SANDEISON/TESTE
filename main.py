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

    def dequeue(self):
        if self.quant == 0:
            print("Fila vazia!")
            return
        valor = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.tamanho
        self.quant -= 1
        return valor
