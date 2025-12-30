# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitando os números do usuário com tratamento de erro
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    # Realizando operações matemáticas básicas
    print("\n--- Resultados das Operações ---")
    print(f"Adição: {numero1} + {numero2} = {numero1 + numero2}")
    print(f"Subtração: {numero1} - {numero2} = {numero1 - numero2}")
    print(f"Multiplicação: {numero1} × {numero2} = {numero1 * numero2}")
    
    # Tratamento especial para divisão por zero
    if numero2 != 0:
        print(f"Divisão: {numero1} ÷ {numero2} = {numero1 / numero2}")
    else:
        print("Divisão: Não é possível dividir por zero!")
    
except ValueError:
    print("Erro: Por favor, digite números válidos!")

# Exemplo de execução:
# Digite o primeiro número: 10
# Digite o segundo número: 5
#
# --- Resultados das Operações ---
# Adição: 10.0 + 5.0 = 15.0
# Subtração: 10.0 - 5.0 = 5.0
# Multiplicação: 10.0 × 5.0 = 50.0
# Divisão: 10.0 ÷ 5.0 = 2.0