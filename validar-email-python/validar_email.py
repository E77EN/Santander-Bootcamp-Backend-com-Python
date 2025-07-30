import re

def validar_email(email):
    """
    Valida se o formato do e-mail está correto.
    
    Args:
        email (str): O endereço de e-mail a ser validado.
    
    Returns:
        bool: True se o e-mail for válido, False caso contrário.
    """
    # Padrão regex para validação básica de e-mail
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return re.match(padrao, email) is not None

def main():
    """
    Função principal para testar a validação de e-mail.
    """
    print("=== Validador de E-mail ===")
    
    while True:
        email = input("\nDigite um e-mail para validar (ou 'sair' para encerrar): ")
        
        if email.lower() == 'sair':
            print("Encerrando o programa...")
            break
        
        if validar_email(email):
            print(f"✓ O e-mail '{email}' é válido!")
        else:
            print(f"✗ O e-mail '{email}' é inválido!")

if __name__ == "__main__":
    main()

