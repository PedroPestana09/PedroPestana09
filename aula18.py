#  Debuger do Visual Studio

# if / elif      / else
# se / se não se / se não

condicao1 = False  # Ao clicar na bola vermelha que aparece antes do numero da linha, marca para programa parar nessa linha de codigo
    # Chama-se de breakpoint. Se não aparecer, ativar nos settings, procurando por "Glyph Margin". Não pára nas linhas de comentários #
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print("Código para condição 1")
elif condicao2:
    print("Código para condição 2")
elif condicao3:
    print("Código para condição 3")
elif condicao4:
    print("Código para condição 4")
else:
    print("Nenhuma condição foi satisfeita")

if 10 == 10:
    print("Outro if")

print("Fora do if")
