# Sistema Bancário em Python Otimizado

Este projeto é um desafio do Bootcamp Santander/DIO, focado na otimização de um sistema bancário simples em Python através da refatoração e implementação de novas funcionalidades.

## Funcionalidades Implementadas

O sistema bancário otimizado possui as seguintes funcionalidades:

- **Depósito**: Permite depositar valores na conta. A função `deposito()` recebe argumentos apenas por posição (`positional only`).
- **Saque**: Permite sacar valores da conta, respeitando limites diários e de valor por saque. A função `saque()` recebe argumentos apenas por nome (`keyword only`).
- **Extrato**: Exibe o histórico de movimentações da conta. A função `extrato()` recebe argumentos por posição e nome (`positional only` e `keyword only`).
- **Criação de Usuário**: Permite cadastrar novos usuários (clientes) com CPF, nome, data de nascimento e endereço. O CPF deve ser único e armazenado apenas com números. A função `criar_usuario()` gerencia o cadastro.
- **Criação de Conta Corrente**: Permite criar novas contas correntes vinculadas a um usuário existente. A função `criar_conta()` associa a conta a um usuário.

## Como usar

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório ou baixe o arquivo `main.py`.
3.  Execute o script Python:
    ```bash
    python3 main.py
    ```
4.  Siga as opções do menu para interagir com o sistema bancário.

## Exemplo de uso

```
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair

=> nu
Informe o CPF (somente números): 12345678900
Informe o nome completo: Teste Usuario
Informe a data de nascimento (dd-mm-aaaa): 01-01-2000
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua Teste, 123 - Bairro - Cidade/SP

Usuário criado com sucesso!
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair

=> nc
Informe o CPF do usuário: 12345678900

Conta criada com sucesso!
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair

=> d
Informe o valor do depósito: 100
Depósito realizado com sucesso!
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair

=> s
Informe o valor do saque: 50
Saque realizado com sucesso!
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair

=> e

========== EXTRATO ==========
Depósito: R$ 100.00
Saque: R$ 50.00

Saldo: R$ 50.00
==============================
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair

=> q
```

