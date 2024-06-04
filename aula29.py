"""
Introdução ao try/except
try -> tentar executar o código (semelhante ao "IF")
except -> quando ocorre algum erro ao tentar executar, vai para aqui (semelhante ao "ELSE")
"""

numero_str = input("Vou dobrar o numero que digitar: ")

try:
    numero_float = float(numero_str)
    print("FLOAT: ", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
except:
    print("Isso não é um numero")
