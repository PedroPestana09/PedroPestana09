"""
    https://docs.python.org/3/library/stdtypes.html
    https://docs.python.org/pt-br/3/library/stdtypes.html
    Tipos de objectos imutáveis (não dá para mudar o valor) que já vimos: str, int, float, bool
    """

string = "Pedro Pestana"
outra_variavel = f"{string[:3]}ABC{string[4:]}"
print(string)
print(outra_variavel)

print(10 * "-")

print(string.zfill(20))
