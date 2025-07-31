# Lista de produtos disponíveis em estoque
estoque = ["Camiseta", "Calça", "Jaqueta", "Tênis", "Boné"]

# Entrada: nome do produto solicitado
produto_solicitado = input()

# Verificação da disponibilidade
if produto_solicitado in estoque:
    print("Produto disponível")
else:
    print("Produto esgotado")


