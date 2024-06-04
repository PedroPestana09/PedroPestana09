nome = "Pedro Pestana"
altura = 1.72
peso = 82
imc = ...  # Os 3 pontos é chamado de Ellipsis, que serve como placeholder, para lembrar de colocar código mais tarde.
# A Ellipsis não gera erro

imc = peso / (altura * altura)  #  imc = peso / (altura x altura)
# Tambem poderia ser feito como: imc = peso / (altura ** 2)
print(imc)

# Fazer um texto que fique como:
# Pedro Pestana tem 1.72 de altura
# pesa 82 quilos e o seu IMC é
# 27.71

print(nome, "tem", altura, "de altura,")
print("pesa", peso, "quilos e o seu IMC é")
print(imc)

