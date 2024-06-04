# Variáveis são usadas para salvar algo na memória do computador. 
# PEP8: inicie variáveis com letras minúsculas, pode usar 
# números e underline _. 
# O sinal de = é o operador de atribuição. Ele é usado para 
# atribuir um valor a um nome (variável). 
# Uso: nome_variavel = expressão (chama-se de snakecase quando uma variavel com palavras em minusculas e separadas por underscore "_")
 
nome = "Pedro Pestana" # variável, neste caso para indicar o nome
idade = 33
peso = 77
maior_de_idade = idade >= 18
obeso = peso > 70
print(nome, idade, peso) # Neste caso, retorna o resultado das respectivas variáveis
print("Nome: ", nome, "-", "Idade: ", idade, "-", "Peso: ", peso, "Kg") # Neste, retorna as strings e o resultado das variáveis
print("Maior de idade? ", maior_de_idade, "Obeso? ", obeso)

