nome = input("Qual o seu nome ? ")

print(f'O seu nome é {nome}')

# Mostra a variavel que foi quardada o respectivo dado:

nome = input("Qual o seu nome ? ")

print(f'O seu nome é {nome=}')

# Um input automaticamente captura os dados em formato de string (str). Para ele fazer uma leitura em outros formatos (p.ex: int, float, boolean...) é necessario especificar o seu formato

# Captura de numeros, porém em formato de string

numero_1 = input("Digite um numero: ")
numero_2 = input("Digite outro numero: ")

print(f'A soma dos números é: {numero_1 + numero_2}')

# A soma acima não é realizada, por que os dados são em formato de string, e por isso é feito apenas uma contatenação entre eles

#Captura de numeros com possivel quebra de codigo (caso for digitado algum dado indesejado):

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

print(f'A soma dos dois numeros é igual a {n1 + n2}')

# Captura de numeros sem quebra de codigo: 

n1 = input("Primeiro número: ")
n2 = input("Segundo número:  ")

int_n1 = int(n1)
int_n2 = int(n2)

print(f'A soma dos dois números é igual a {int_n1 + int_n2}')