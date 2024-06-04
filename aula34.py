"""
Repetições
while (enquanto) - Executa uma acção enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim. Ter cuidado!
"""

condicao = True

while condicao:
    nome = input("Qual o seu nome: ")
    print(f"Seu nome é {nome}")
# Ficará sempre em loop até a condição for Falsa ou usando um comando "break"
    if nome == "sair":
        break

print("Acabou")
