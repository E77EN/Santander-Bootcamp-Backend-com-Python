# Dados cadastrados (usuários e suas senhas)
usuarios = {
    "joao": "1234",
    "maria": "senha123"
}

# Leitura da entrada
usuario_input = input().strip()
senha_input = input().strip()

# Verificação
if usuario_input in usuarios and usuarios[usuario_input] == senha_input:
    print("Acesso permitido")
else:
    print("Usuário ou senha incorretos")
