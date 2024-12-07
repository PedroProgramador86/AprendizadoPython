# if  /   elif    / else
# se / Se não se / se não

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('Este é um codigo do if')

print("Comando fora do if")

# Condiçao falsa

condicao = False

if condicao2:
    print('Este é um codigo do if')

else:
    print("Este é o else do primeiro if")

if 10 == 10:
    print("Outro if")

print("Comando fora do if")


vf = input("Digite True ou False: ")

if vf == "True":
    print("Essa condição é verdadeira")

elif vf == "False":
    print("Essa condição é falsa")

else:
    print("Nenhuma das respostas é satisfatoria...")