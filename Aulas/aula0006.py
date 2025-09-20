# Conversão de tipos, coerção, type convertion, typecasting, coersion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1)
#print('1' + 1) #Codigo com erro
print(int('1') + 1) #<- Entender isso é importante, pois quando pedimos um determinado dado ao usuario em "str" podemos até (as vezes) converte-lo em um tipo numerico
#print(int('P') + 1) #Codigo com erro
print(int('1'), type(int('1')))
print('a' + 'b')

print(bool("")) #String vazia é considerada como falsa
print(bool(" ")) #String que contenha pelo menos um espaço, é considerada como verdadeira

print(str(12) + 'p')
