"""
CONSTANTE = Usar letras maiusculas em variáveis que não pretendemos mudar o valor. 
            Isto é para indicar tanto para nós como para outros programadores.

"\" serve para criar uma quebra de linha no código e podermos continuar a escrever na linha seguinte abaixo

Muitas condições no mesmo if (mau - ruim). Torna-se complicado de ler e podemos originar erros. Tentar manter simples/clean.

    <- Contagem de complexidade. Quanto mais afastado da margem, mais complexo (mau - ruim)
"""

velocidade = 61  # Velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

# Usar letras maiusculas em variáveis que não pretendemos mudar o valor. Isto é para indicar tanto para nós como para outros programadores.
RADAR_1 = 60  # velocidade máxima do radar 1 
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distancia onde o radar pega

# Exemplo de código, mas que pode ser optimizado:
# if velocidade > RADAR_1:
#     print("Excesso de velocidade no radar 1")
# # \ serve para criar uma quebra de linha no código e podermos continuar a escrever na linha seguinte abaixo
# if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#     local_carro <= (LOCAL_1 + RADAR_RANGE) and \
#         velocidade > RADAR_1:
#     print("Carro multado no radar 1")

print("Código mais clean e simples")

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print("Excesso de velocidade no radar 1")

if carro_passou_radar_1:
    print("Carro passou no radar 1")

if carro_multado_radar_1:
    print("Carro multado no radar 1")