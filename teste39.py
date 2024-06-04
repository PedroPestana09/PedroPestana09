"""
Iterando strings com while
"""

#       0123456789101112
nome = "Pedro Pestana"  # Iteráveis
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[6])

indice = 0
novo_nome = ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"*{letra}"  # Ao colocar o asterisco *, acrescenta o mesmo a cada letra
    indice += 1

novo_nome += "*"  # Para acrescentar um asterisco no fim da última letra
print(novo_nome)
