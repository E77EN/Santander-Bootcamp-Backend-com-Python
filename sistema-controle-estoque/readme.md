# Desafio: Verificador de Estoque

Este projeto é um exercício de lógica de programação que simula um sistema simples de verificação de estoque para uma loja.

## 🎯 Objetivo do Projeto

O desafio consiste em criar um programa que, a partir de uma lista pré-definida de produtos em estoque, verifique se um item solicitado pelo usuário está disponível. O objetivo principal é exercitar o uso de estruturas de dados (listas) e a lógica condicional.

## 🛠️ Conceitos Aplicados

*   **Estrutura de Dados (Lista):** O programa utiliza uma lista em Python para armazenar os nomes dos produtos disponíveis, representando o estoque da loja.
*   **Operador de Inclusão (`in`):** A verificação de disponibilidade é feita de forma eficiente e legível utilizando o operador `in`, que checa se um elemento existe dentro de uma coleção.
*   **Lógica Condicional (`if/else`):** Uma estrutura condicional é usada para determinar qual mensagem deve ser exibida ao usuário, com base no resultado da verificação de estoque.
*   **Entrada do Usuário (`input`):** O programa interage com o usuário lendo o nome do produto solicitado através da função `input()`.

## 📋 Exemplos de Execução

A tabela abaixo ilustra o comportamento esperado do programa, considerando uma lista de estoque pré-definida.

| Produto Solicitado (Entrada) | Saída Esperada      |
| :--------------------------- | :------------------ |
| `Camiseta`                   | Produto disponível  |
| `Jaqueta`                    | Produto disponível  |
| `Vestido`                    | Produto esgotado    |

---
