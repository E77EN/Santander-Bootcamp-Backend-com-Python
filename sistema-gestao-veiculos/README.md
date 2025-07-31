
# Desafio: Sistema de Gestão de Veículos

Este projeto demonstra a aplicação prática de **Programação Orientada a Objetos (POO)** e a implementação de padrões de código para a resolução de um problema específico.

## 🎯 Objetivo do Projeto

O desafio consiste em desenvolver uma classe `Veiculo` em Python que encapsule os dados e comportamentos de um carro. A implementação deve seguir os princípios da orientação a objetos para criar um código limpo, reutilizável e de fácil manutenção.

O sistema deve ser capaz de:
1.  Representar um veículo com os atributos `marca`, `modelo` e `ano`.
2.  Implementar um método que avalia a idade do veículo e o classifica como "antigo" ou "novo".

## 🛠️ Conceitos Aplicados

*   **Orientação a Objetos:**
    *   **Classe e Objeto:** Utilização da classe `Veiculo` como um molde para criar instâncias (objetos) que representam carros específicos.
    *   **Encapsulamento:** Agrupamento dos atributos (`marca`, `modelo`, `ano`) e métodos (`verificar_idade`) dentro de uma única unidade lógica, a classe `Veiculo`.
*   **Padrões de Código:**
    *   **Lógica de Negócio:** O método de verificação de idade implementa uma regra de negócio clara: um carro com mais de 20 anos é considerado antigo.
    *   **Entrada e Saída Padronizadas:** O código foi estruturado para processar entradas específicas e gerar saídas que seguem um formato rigoroso, garantindo a consistência e a previsibilidade do programa.

## 📋 Exemplos de Execução

A tabela abaixo ilustra o comportamento esperado do programa com base em diferentes entradas:

| Marca  | Modelo  | Ano  | Saída Esperada |
| :----- | :------ | :--- | :------------- |
| Toyota | Corolla | 2000 | Veículo antigo |
| Honda  | Civic   | 2005 | Veículo novo   |
| Ford   | Fiesta  | 1999 | Veículo antigo |

