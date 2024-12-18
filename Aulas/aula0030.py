"""
CONSTANTE = "Variaveis" que não vão mudar
(Para uma melhor interpretação, elabore variaveis consideradas constantes deixando todas as letras captalizadas)

Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

# velocidade = 61 # velocidade atual do carro
# local_carro = 101 # local em que o carro está na estrada

# RADAR_1 = 60 # Velocidade máxima do radar 1
# LOCAL_1 = 100 # Local onde o radar 1 está
# RADAR_RANGE = 1 # A distância onde o radar pega

# if (velocidade > RADAR_1):
#     print("A velocidade do carro passou do radar 1")

# if (local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)):

#     print("Carro multado em radar 1 !")

#//////////////////


# velocidade = 60 # velocidade atual do carro
# local_carro = 101 # local em que o carro está na estrada

# RADAR_1 = 60 # Velocidade máxima do radar 1
# LOCAL_1 = 100 # Local onde o radar 1 está
# RADAR_RANGE = 1 # A distância onde o radar pega

# if (velocidade > RADAR_1):
#     print("A velocidade do carro passou do radar 1")

# if (local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1):

#     print("Carro multado em radar 1 !")

# Refazendo o codigo com mais logica e consequentemente mais variaveis:

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

carro_passou_no_limite_do_radar = velocidade > RADAR_1

if (carro_passou_no_limite_do_radar):
    print("A velocidade do carro passou do radar 1")

carro_passou_no_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_levou_multa = carro_passou_no_radar_1 and carro_passou_no_limite_do_radar

if (carro_levou_multa):

    print("Carro multado em radar 1 !")