# Agora vamos calcular a média de três notas fornecidas na entrada do usuário.
# Utilize operadores aritméticos para realizar o cálculo da média.

# Solicitando as três notas do usuário
try:
    print("Digite as três notas (0 a 10):")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    # Validando se as notas estão entre 0 e 10
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        print("Erro: As notas devem estar entre 0 e 10!")
    else:
        # Calculando a média usando operadores aritméticos
        media = (nota1 + nota2 + nota3) / 3
        
        # Exibindo o resultado formatado com 2 casas decimais
        print(f"\nMédia das notas: {media:.2f}")
        
        # Bonus: Classificação da média
        if media >= 7:
            print("Situação: APROVADO! 🎉")
        elif media >= 5:
            print("Situação: RECUPERAÇÃO ⚠️")
        else:
            print("Situação: REPROVADO 😞")
    
except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos!")

# Exemplo de execução:
# Digite as três notas (0 a 10):
# Nota 1: 8.5
# Nota 2: 7.0
# Nota 3: 9.0
#
# Média das notas: 8.17
# Situação: APROVADO! 🎉
