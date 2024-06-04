# Operadores lógicos - continuação
# and (e); or (ou); not (não)
# not - Usado para inverter expressões.
# not True = False
# not False = True

print(not True)  # Resultado vai ser False
print(not False)  # Resultado vai ser True

senha = input("Senha: ")
if not senha:  # Se não for digitada nenhuma senha, irá apresentar a string abaixo.
    print("Você não digitou nada")
