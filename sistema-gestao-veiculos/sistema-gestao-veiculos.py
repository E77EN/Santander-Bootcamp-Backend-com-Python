import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def verificar_antiguidade(self):
        ano_atual = datetime.datetime.now().year
        if ano_atual - self.ano > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

marca = input()
modelo = input()
ano = int(input())

veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())



