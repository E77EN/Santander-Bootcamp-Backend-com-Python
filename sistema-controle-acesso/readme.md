# Desafio: Sistema de Login Simples

Este projeto implementa um sistema de verificação de login, um exercício fundamental para praticar a manipulação de entradas do usuário e a lógica condicional em Python.

## 🎯 Objetivo do Projeto

O desafio consiste em criar um programa que simule uma verificação de login. Diferente de um sistema real com um banco de dados fixo, este programa é projetado para um ambiente de testes onde as credenciais "corretas" são fornecidas como parte da entrada.

O sistema deve:
1.  Ler um nome de usuário e uma senha que serão considerados os dados "cadastrados" para aquele teste específico.
2.  Ler um segundo par de nome de usuário e senha, que representam a tentativa de login do usuário.
3.  Comparar os dois conjuntos de credenciais e determinar se o acesso deve ser permitido.

## 🛠️ Conceitos Aplicados

*   **Lógica Condicional:** O núcleo do programa é uma estrutura `if/else` que utiliza o operador `and` para verificar se tanto o nome de usuário quanto a senha da tentativa de login correspondem exatamente às credenciais cadastradas.
*   **Processamento de Entrada Sequencial:** O código é estruturado para ler quatro linhas de entrada em uma ordem específica, armazenando-as em variáveis distintas para a comparação posterior.
*   **Comparação de Strings:** A lógica se baseia na comparação exata de strings para validar as credenciais, um princípio básico em qualquer sistema de autenticação.

## 📋 Exemplos de Execução

A tabela abaixo ilustra o comportamento esperado do programa. Note que as duas primeiras linhas de entrada definem as credenciais válidas para o teste, e as duas linhas seguintes são a tentativa de login.

| Entrada (4 linhas)                                   | Saída Esperada                |
| :--------------------------------------------------- | :---------------------------- |
| `joao`  
`1234`  
`joao`  
`1234`                  | `Acesso permitido`            |
| `maria`  
`senha123`  
`maria`  
`senha123`        | `Acesso permitido`            |
| `joao`  
`1234`  
`ana`  
`1234`                   | `Usuário ou senha incorretos` |

---
