# Desafio: Sistema de Pedidos de Restaurante

Este projeto implementa uma solução em Python para calcular o valor total de um pedido em um restaurante, utilizando os princípios da **Programação Orientada a Objetos (POO)** para estruturar o código de forma clara e eficiente.

## 🎯 Objetivo do Projeto

O desafio consiste em criar uma classe `Pedido` que seja capaz de gerenciar os itens de um pedido e calcular o valor total da conta. O sistema deve ser projetado para lidar com um número variável de itens, processando seus nomes e preços.

## 🛠️ Conceitos Aplicados

*   **Programação Orientada a Objetos:**
    *   **Classe `Pedido`:** Centraliza a lógica do negócio, encapsulando a lista de itens e o método para o cálculo do total.
    *   **Métodos:** O método `calcular_total()` abstrai a complexidade da soma, oferecendo uma interface simples para obter o resultado final.
*   **Estrutura de Dados:**
    *   Utilização de uma lista para armazenar os itens do pedido, demonstrando a manipulação de coleções de dados.
*   **Processamento de Entrada:**
    *   O código é estruturado para ler e interpretar múltiplas linhas de entrada (o número de itens, seguido pelos próprios itens e seus preços), um padrão comum em desafios de programação.
*   **Manipulação de Strings e Tipos:**
    *   O programa processa cada linha de entrada, separando o nome do item (string) do seu preço (float) para realizar os cálculos corretamente.

## 📋 Exemplos de Execução

A tabela abaixo detalha o comportamento esperado do programa, conforme a descrição do desafio:

| Entrada                                                              | Saída Esperada |
| :------------------------------------------------------------------- | :------------- |
| `2`  
`Pizza 40.00`  
`Suco 7.50`                                   | `47.50`        |
| `3`  
`Hamburguer 15.50`  
`Refrigerante 5.00`  
`Batata 8.00`      | `28.50`        |
| `4`  
`Café 4.50`  
`Pão de queijo 6.00`  
`Bolo 10.25`  
`Chá 3.75` | `24.50`        |

---
