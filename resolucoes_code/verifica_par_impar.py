# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.
# Utilize condicionais para realizar a verificação.

# Solicitando um número inteiro do usuário
try:
    numero = int(input("Digite um número inteiro: "))
    
    # Utilizando o operador de módulo (%) para verificar se é par ou ímpar
    # Se o resto da divisão por 2 for 0, o número é par
    if numero % 2 == 0:
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é ÍMPAR!")
    
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido!")

# Exemplo de execução:
# Digite um número inteiro: 8
# O número 8 é PAR!
#
# Digite um número inteiro: 7
# O número 7 é ÍMPAR!
#
# Explicação:
# O operador % (módulo) retorna o resto da divisão
# 8 % 2 = 0 (par)
# 7 % 2 = 1 (ímpar)
