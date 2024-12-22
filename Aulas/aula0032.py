"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite um numero inteiro: ")

# try:

#     numero_inteiro = int(numero)

#     if(numero_inteiro % 2 == 0):

#         print("O numero digitado é par !")

#     elif(numero_inteiro % 2 == 1):

#         print("O numero digitado é impar !")

# except:

#     print("Você não digitou um numero inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# nome = input("Digite o seu nome: ")
# nome_str = str(nome)

# horario = input("Digite o horario atual: ")
# horario_int = int(horario)

# try:

#     if(horario_int >= 0 and horario_int <= 11):
#         print(f"Bom dia {nome_str}")

#     elif(horario_int >= 12 and horario_int <= 17):
#         print(f"Boa tarde {nome_str}")

#     elif(horario_int >= 18 and horario_int <= 23):
#         print(f"Boa noite {nome_str}")

# except:
     
#     print("Valor invalido !")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite o seu nome: ")
nome_str = str(nome)

contagem_nome = len(nome_str)

if(contagem_nome > 0 and contagem_nome <= 4):
    print("Seu nome é curto !")

elif(contagem_nome >= 5 and contagem_nome <= 6):
    print("Seu nome tem o tamanho normal !")

elif(contagem_nome > 6 ):
    print("Seu nome é muito grande !")

elif(contagem_nome == 0 ):
    print("Você não digitou um nome...")
