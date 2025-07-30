descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

preco_original = float(input())
cupom = input().strip().upper()

if cupom in descontos:
    desconto = descontos[cupom]
    preco_final = preco_original * (1 - desconto)
else:
    preco_final = preco_original

print(f"{preco_final:.2f}")

