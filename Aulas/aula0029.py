"""
Introdução ao Try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(1234567)
# print(29403)
# int('a')

# Teste de dobrar um numero:

# numero = input("Digite um número: ")

# print(f"São apenas numeros: {numero.isdigit()}")
# # OBS: "isdigit()" é uma função do python que faz uma verificação de caso os valores mensionados em determinada variavel são APENAS numeros (Ou seja, qualquer caractere que não seja um numero é dado como "false". Isso inclui o "." de um numero flutuante)


# numero_float = float(numero)
# print(f"O dobro de {numero} é igual a {numero_float * 2:.2f}")

# Teste de dobrar um numero:

# numero = input("Digite um número: ")

# if(numero.isdigit()):
#     numero_float = float(numero)
#     print(f"O dobro de {numero} é igual a {numero_float * 2:.2f}")

# else:
#     print("Isso não é um número")



# Fazendo o uso do "try" e "except":

# try:
#     ...
# except:
#     ...

# Por questões de sintaxe, o "try" e "except". Pedem obrigatoriamente que tenha algum valor dentro de seu espaço para codigo

# Demonstração de como funciona o "try" e "exepty" e até onde o codigo com erro pode chegar:


numero = input("Digite um numero: ")

try:

    print("=== Numero em estado de String ===")
    numero_float = float(numero)
    print("=== Numero em estado de Flutuante ===")
    print(f"O numero {numero} tem como valor dobrado {numero_float * 2}")

except:

    print("Isso não é um numero...")
