class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)

    def verificar_antiguidade(self):
        ano_base = 2024  # Use o ano que a plataforma estiver usando para testar
        if ano_base - self.ano > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

# Entrada padrão via input
marca = input()
modelo = input()
ano = input()

# Criação do objeto e saída
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
