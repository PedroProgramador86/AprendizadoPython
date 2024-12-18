"""
Fatiamento de strings

 012345678
 Olá Mundo
-987654321

Fatiamento [i:f:p] [::]
(i = Inicio)
(f = fim)
(p - passo)

Obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = "Olá Mundo"

#Printando a letra "u" da variavel "variavel" porém de formas diferentes:
print(variavel[5])
print(variavel[-4])

#Usando fatiamento:

#De um inicio determinado até o fim:
print(variavel[4:])

#OBS: Sempre que quiser ser especifico no final, você precisa mensionar o (indice + 1)
#P.ex: Para pegar o "o" de mundo, que está localizado no indice 8, precisaria somar +1 ao indice mensionado (8). Senão ele mensionaria o indice "d" no final.

#Com o indice mensionado:
print(variavel[4:8])

#Com o indice mensionado +1:
print(variavel[4:9])


#Do Inicio até um fim determinado:
print(variavel[:3])

# Função len:

print(len(variavel))

print(variavel[0:len(variavel):1])
print(variavel[0:9:1])
print(variavel[0:9:2])

print(variavel[::-1])
print(variavel[-1:-10:-1])