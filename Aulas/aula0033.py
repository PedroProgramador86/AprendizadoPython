"""

https://docs.python.org/pt-br/3/library/stdtypes.html
Imutveis que vimos: str, int, float, bool

"""

# Não é possivel fazer alterações por que o dado é imutavel:

#p.ex:


string = 'pedro enzo'
string2 = "PEDRO ENZO"
outra_variavel = string

# string[3] = 'ABC'
# print(string[4])

print(outra_variavel)
print(string.capitalize())
print(string.isupper())
print(string2.isupper())
