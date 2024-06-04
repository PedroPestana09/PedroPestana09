"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]  - i= inicio - f= fim - p= passo, de quantos em quantos caracteres ele pula/passa, por defeito vai de 1 em 1 
Obs.: A função len retorna a qtd de caracteres da str
"""

variavel = "Olá mundo"
print(variavel[5])  # Usa-se [] com o numero do indice (positivo ou negativo) para mostrar o caracter nessa localização dessa string

print(variavel[4:8])  # Indica qual o inicio e o fim da string a mostrar, sendo que nunca mostra o caracter do indice final

print(variavel[4:])  # Indica qual o inicio mas, como não indica qual é o fim, mostra tudo até ao fim da string.

print(variavel[:5])  # Indica qual o fim mas, como não indica qual é o inicio, mostra tudo desde o inicio da string.
# Tambem podia ser [0:5], sendo o zero o inicio da string.

print(len(variavel))  # Função len diz quantos caracteres tem, neste caso a string da variavel "Olá mundo" (Também conta com o espaço)

print(variavel[0:len(variavel):1])  # Fatiamento p de 1 em 1. Tambem poderia ter sido: print(variavel[0:9:1])

print(10 * "-")
print("Fatiamento de 2 em 2")
print(variavel[0:len(variavel):2])  # Fatiamento p de 2 em 2.

print(10 * "-")
print(variavel[-1:-10:-1])  # p-1 Indica para começar do fim para a o inicio de caracter em caracter.
# Tambem podia ser print(variavel[::-1]).
