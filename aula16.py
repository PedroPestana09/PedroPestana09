#  Operações condicionais

# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == "entrar" :  # é uma condição que pode ser usada sem mais nenhuma das outras
    print("Você entrou no sistema")  # Usar TAB no inicio para dar vários espaços e pertencer à condição acima
    print("Bem vindo")
elif entrada == "sair" :  # é uma condição que obriga a um if e pode ser repetido várias vezes
    print("Você saiu do sistema")
    print(321)
else:  # é uma condição que obriga a um if, não obriga a elif e, a ser usado, é sempre o último
    print("Você não digitou nem entrar e nem sair.")
print("Fora dos blocos acima")  # Não usar TAB no inicio para não pertencer à condição acima
