#  Coletar dados do nosso utilizador usando a função input
#  input("Qual o seu nome? ")  # O programa não finaliza. Só após o utilizador digitar algo (mesmo que seja apenas clicar no ENTER)
nome = input("Qual o seu nome? ")  # Poderá ser usado com uma variável ex: nome
print(f"O seu nome é {nome}")

numero_1 = input("Digite um numero: ")
numero_2 = input("Digite outro numero: ")
print(f"A soma dos números é: {numero_1 + numero_2}")  # Como são strings, ele vai fazer a concatenação (mostrar os 2 numeros juntos)

numero_1 = int(input("Digite um numero: "))  # Uma das soluções era alterar o tipo, neste caso para int (numero inteiro)
numero_2 = int(input("Digite outro numero: "))
print(f"A soma dos números é: {numero_1 + numero_2}")  # Agora já vai somar os 2 numeros, mas pode dar erro se o utilizador escrever uma letra!

nome = input("Digite o seu nome: ")
apelido = input("Digite o seu apelido: ")
print(f"Nome completo: {nome + apelido}")
