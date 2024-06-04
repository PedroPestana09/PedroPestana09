"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é e não é (tipo, valor, identidade)
id = Identidade
"""
print("Algoritimo - código para solucionar um determinado problema")

# id mostra a identidade da variavel na memória
variavel_1 = "a"
variavel_2 = "a"
print(id(variavel_1))  # se os valores forem os mesmos de diferentes variáveis, o ID vai ser o mesmo, para poupar recursos.
print(id(variavel_2))  # só se os valores forem diferentes é que o ID também vai ser diferente

print(10 * "-")
# Criar condições/flag/bandeira para marcar se programa passa por aqui 
condicao = True  # Se condição for False, muda a flag.
passou_no_if = None

if condicao:
  passou_no_if = True
  print("Faça algo")
else:
  print("Não faça algo")

if passou_no_if is None:
  print("Não passou no if")

else:  # Tambem podia ser - if passou_no_if is not None:
  print("Passou no if")