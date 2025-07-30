num_produtos = int(input())

produtos = []
for _ in range(num_produtos):
    linha = input().split(" ")
    nome = linha[0]
    preco = float(linha[1])
    produtos.append((nome, preco))

total_compra = 0
for nome, preco in produtos:
    print(f"{nome}: R${preco:.2f}")
    total_compra += preco

print(f"Total: R${total_compra:.2f}")

