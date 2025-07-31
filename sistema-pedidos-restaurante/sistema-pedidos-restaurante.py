class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco):
        self.itens.append({'nome': nome, 'preco': preco})

    def calcular_total(self):
        total = 0.0
        for item in self.itens:
            total += item['preco']
        return total

pedido = Pedido()

n = int(input())

for _ in range(n):
    nome_item, preco_item = input().rsplit(' ', 1)
    pedido.adicionar_item(nome_item, float(preco_item))

total_do_pedido = pedido.calcular_total()
print(f"{total_do_pedido:.2f}")

