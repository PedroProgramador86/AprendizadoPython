"""

Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""

nome = 'Pedro'
preco = 1000.923433
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print("O Hexadecimal de %d é %x" % (15, 15))

print("O hexadecimal de %d é %08x" % (1500, 1500))