# Vamos testar se uma palavra é um palíndromo?!
# Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Solicitando uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Removendo espaços e convertendo para minúsculas para comparação uniforme
palavra_tratada = palavra.replace(" ", "").lower()

# Invertendo a string usando slicing [::-1]
palavra_invertida = palavra_tratada[::-1]

# Comparando a palavra original (tratada) com a invertida
if palavra_tratada == palavra_invertida:
    print(f"✅ '{palavra}' é um PALÍNDROMO!")
else:
    print(f"❌ '{palavra}' NÃO é um palíndromo.")

# Mostrando a palavra invertida para visualização
print(f"Palavra original: {palavra_tratada}")
print(f"Palavra invertida: {palavra_invertida}")

# Exemplo de execução:
# Digite uma palavra: arara
# ✅ 'arara' é um PALÍNDROMO!
# Palavra original: arara
# Palavra invertida: arara
#
# Digite uma palavra: Ovo
# ✅ 'Ovo' é um PALÍNDROMO!
# Palavra original: ovo
# Palavra invertida: ovo
#
# Digite uma palavra: python
# ❌ 'python' NÃO é um palíndromo.
# Palavra original: python
# Palavra invertida: nohtyp
#
# Explicação:
# [::-1] é uma técnica de slicing que inverte a string
# [início:fim:passo] -> [::-1] significa "do início ao fim com passo -1"
