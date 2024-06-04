if 0 and 1:
    print(True and 1)  # Não será exibido nada porque a expressão acima tem um Falsy (0 zero)

if 1 and 1:
    print(True and 1 and 0.0) # Será exibido 0.0 porque é o Falsy na expressão
