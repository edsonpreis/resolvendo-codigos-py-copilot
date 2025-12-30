# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

# Solicitando os dois dados do usuário
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatenando os dados em uma única string
resultado = dado1 + dado2

# Exibindo o resultado
print("Resultado da concatenação:", resultado)

# Exemplo de execução:
# Digite o primeiro dado: Olá
# Digite o segundo dado: Mundo
# Resultado da concatenação: OláMundo
#
# Para concatenar com espaço, você pode usar:
# resultado = dado1 + " " + dado2
# ou usar f-strings:
# resultado = f"{dado1} {dado2}"