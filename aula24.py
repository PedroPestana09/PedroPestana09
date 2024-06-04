# Operadores in (está entre) e not in (não está entre)
# Strings são iteráveis (item por item)
#  0 1 2 3 4
#  P e d r o  # Usando indices (positivos ou negativos) para relacionar a posição, exemplo o P está no indice 0, o d está no indice 2.
# -5-4-3-2-1  # No indice negativo, o P está no indice -5 e o d está no -3.

nome = "Pedro"
print(nome[2])  # Os pararenteses rectos [] servem para identificar qual o indice
print(nome[-3])

print(10 * "-")

print("dr" in nome)  # Se a letra ou palavra da string estiver na variável, informa True.
print("k" in nome)  # Se a letra ou palavra da string não estiver na variável, informa False.

print(10 * "-")

print("ze" not in nome)  # Se a letra ou palavra da string não estiver na variável, informa True.
print("dr" not in nome)  # Se a letra ou palavra da string estiver na variável, informa False.

print(10 * "-")

nome = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")
