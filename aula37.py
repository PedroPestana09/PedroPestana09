# Com o while, podemos usar continue para saltar, ou o break para parar.

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("Não mostrar o 6.")
        continue

    if contador >= 10 and contador <= 37:
        # print("Não mostrar o ", contador)
        continue

    print(contador)

    if contador == 40:
        break

print("Acabou")
