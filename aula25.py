"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Pedro"
preco = 2496.65987
variavel = "%s, o preço é €%.2f" % (nome, preco)
print(variavel)

print(10 * "-")

print("O hexadecimal de %d é %x" % (15, 15))
print("O hexadecimal de %d é %04x" % (15, 15))   # Colocar o numero de casas decimas que pretendemos no hexadecimal, ao colocar por exemplo %04x.
print("O hexadecimal de %d é %08X" % (255, 255))   # Colocar o X maiusculo, para o hexadecimal ser escrito em maiusculas.
