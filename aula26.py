"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f - numero de digitos que pretendemos que sejam visualizados
x ou X - Hexadecimal
(Caractere)(><^)(quantidade) - 
> - Esquerda
< - Direita
^ - Centro
= - Força o numero a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")  # Ao colocar >numero, irá colocar a variável à direita, com x caracteres à esquerda da mesma.

print(f"{variavel: <6}.")  # Ao colocar <numero, irá colocar a variável à esquerda, com x caracteres à direita da mesma.
# Colocado um ponto "." para mostrar onde termina.

print(f"{variavel:$^10}")  # Ao colocar ^numero, irá colocar a variável ao centro do numero de caracteres definido.
# Se colocarmos algum caracter, este será exibido

print(f"{123456.43543578:,.3f}")  # :,.3f - A virgula divide os milhares, o ponto e depois o numero de quantas casas decimais pretendemos mostrar.

print(f"{123456.43543578:0=+10,.2f}")  # O sinal de + força a aparecer o simbolo quando o numero é positivo.
# O igual, força o simbolo (positivo ou negativo) a aparecer antes do numero.

print(f"O hexadecimal de 1500 é {1500:08x}")  # Mostra o numero em hexadeximal minusculo e com 8 casas decimais.
