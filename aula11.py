# Precedencia/prioridade de uns operadores sobre os outros
# 1º coisas que estão dentro de parenteses -> ()
# 2º depois a potenciação ou exponenciação -> **
# 3º depois a multiplicação, a divisão, a divisão inteira e o modulo -> * / // %
# 4º por fim a adição e a subtração -> + -
# 
print(2 ** 10)  # 2 elevado a 10 é igual a 1024

conta_1 = 1 + 1 ** 5 + 5  # se fizermos esta conta, o resultado não vai dar 1024, mas 7, por causa da precedencia/prioridade
print(conta_1)

conta_1 = (1 + 1) ** (5 + 5)  # alterando e colocando desta forma, o resultado já vai dar 1024
print(conta_1)