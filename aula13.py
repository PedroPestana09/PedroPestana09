# Formatação de Strings
# Exemplo de uma chamada de F-Strings
nome = "Pedro Pestana"
altura = 1.725
valor_2 = 123456789
peso = 82
imc = peso / (altura * altura) 
# print(nome, "tem", altura, "de altura,")
# print("pesa", peso, "quilos e o seu IMC é")
# print(imc)


# Ao invés de escrever da forma anterior, também se pode fazer usando uma F-String
# Coloca-se um f no inicio da String, que permite a possibilidade de usar variáveis dentro do texto/string
# Depois, para usar variáveis, colocar chavetas {} antes e depois do texto que representa a variável
linha_1 = f"{nome} tem {altura} de altura"  
linha_2 = f"{altura:.2f}"  # Se quisermos limitar o numero de casas decimais, colocar :.xf, onde x é o nº de casas decimais
linha_3 = f"{valor_2:,.1f}"  # Se quisermos identificar o numero da casa de milhares, colocar :,f. Colocar também .xf por causa das casas decimais
print(linha_1)
print(linha_2)
print(linha_3)

linha_4 = f"pesa {peso} quilos e o seu IMC é"
linha_5 = f"{imc:.2f}"
print(linha_1)
print(linha_4)
print(linha_5)
