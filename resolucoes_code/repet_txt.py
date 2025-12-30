# Agora vamos solicitar uma string e um número inteiro como entrada.
# Depois teremos que retornar a string repetida o número de vezes informado.

# Solicitando a string do usuário
texto = input("Digite um texto: ")

# Solicitando o número de repetições com tratamento de erro
try:
    repeticoes = int(input("Digite o número de repetições: "))
    
    # Verificando se o número é positivo
    if repeticoes < 0:
        print("Erro: O número de repetições deve ser positivo!")
    else:
        # Repetindo o texto
        resultado = texto * repeticoes
        print("Resultado:", resultado)
        
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido!")

# Exemplo de execução:
# Digite um texto: Python
# Digite o número de repetições: 3
# Resultado: PythonPythonPython
#
# Para repetir com espaço entre as repetições:
# resultado = (texto + " ") * repeticoes