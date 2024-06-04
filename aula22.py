# Operadores lógicos - continuação
# and (e); or (ou); not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy (como falsos): 0 - 0.0 - "" (sem espaço entre as aspas) - False
# Também existe o tipo None que é usado para representar um não valor

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

# if entrada == "E" or entrada == "e" and senha_digitada == senha_permitida:  # Assim também seria executado mas fica muito complicado
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:  # O or permite uma variável ou outra.
    print("Entrar")
else:
    print("Sair")

# Avaliação de curto circuito - quando detecta um valor na expressão que corresponde a True ou False, ele pára e já não lê mais nada para a frente.
print(0 or False or "abcd" or False)  # Exibe o primeiro valor verdadeiro, neste caso, abcd.

senha = input("Senha: ") or "Sem senha"  # Se não for digitada senha, apresenta string "Sem senha"
print(senha)
