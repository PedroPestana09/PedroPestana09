# Formatar usando a função Format

a = "AAAA"
b = "B"
c = 1.1
string = "b={nome2}  a={0} b={0} b={nome2} c={nome3:.2f}"
formato = string.format(a, nome2=b, nome3=c)  # nome2 e nome3 são chamados de parametros nomeados
print(formato)
