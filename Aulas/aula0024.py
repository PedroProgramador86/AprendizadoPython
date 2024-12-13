# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4
#  P e d r o
# -5-4-3-2-1

# nome = 'Pedro'

# print(nome[3])
# print(nome[-2])

# print(10 * '-')

# print('P' in nome)
# print('p' in nome)
# print('t' in nome)
# print('edro' in nome)

# print('teto' not in nome)
# print('s' not in nome)

nome = input("Digite o seu nome: ")

encontrar = input("Digite oque você quer encontrar: ")

if encontrar in nome:
    
    print(f"{encontrar} está em {nome}")

else:

    print(f"{encontrar} não está em {nome}")