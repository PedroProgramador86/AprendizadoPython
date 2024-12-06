a = 'Pedro'
b = 'Enzo'
c = 18.86

string = 'a = {} b = {} c = {:.3f}'
formatacao = string.format(a, b, c)

print(formatacao)

#Tudo em python é um objeto, e geralmente objetos tem "metodos" (Ou "method" como o proprio python chama) que são ações dentro deles.

#Ou seja, para chamar uma função de um objeto em python, é necessario colocar um "." depois dele e assim mencionar a função que deseja atribuir

#No caso do exemplo acima foi o "format" por cima da variavel (objeto) string.

#Ordenando por indices:

a = 'Pedro'
b = 'Enzo'
c = 18.86

#Agora é possivel alterar a ordem do que vai aparecer primeiro nos parametos

string = 'a = {0} b = {1} c = {2:.3f}'
formatacao = string.format(a, b, c)

print(formatacao)

# "Parametro nomeado" é quando é dado um nome para as coisas das chamadas funções

a = 'Pedro'
b = 'Enzo'
c = 18.86

string = 'a = {} b = {variavel2} c = {variavel3:.3f}'
formatacao = string.format(a, variavel2 = b, variavel3 = c)

print(formatacao)

#Embaralhando a ordem:

a = 'Pedro'
b = 'Enzo'
c = 18.86

string = 'b = {variavel2} c = {variavel3} a = {}'
formatacao = string.format(a, variavel2 = b, variavel3 = c)

print(formatacao)