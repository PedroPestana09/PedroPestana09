# Operadores lógicos
# and (e); or (ou); not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor (como falso)
# São considerados falsy (como falsos): 0 - 0.0 - "" (sem espaço entre as aspas) - False
# Também existe o tipo None que é usado para representar um não valor

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if entrada == "E" and senha_digitada == senha_permitida:  # O if só será executado se toda a expressão for True
    print("Entrar")
else:
    print("Sair")

# Avaliação de curto circuito - quando detecta um valor na expressão que corresponde a True ou False, ele pára e já não lê mais nada para a frente.
print(True and False and True and True)
print(True and 0 and True and True)

# Valor Falsy
print(bool(0.0))
