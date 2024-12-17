"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - (+ ou -)
Ex: 0>-100,.1f
Conversion flags - !r (metodo "repr") !s (metodo "str") !a (metodo "ASCII")
"""

variavel = "ABC"
print(f'{variavel}')

#Faz o preenchimento de uma quantidade especificada (no caso o espaço "10") de uma certa coisa (espaços " ") ao lado mencionado (> A esquerda): 
print(f'{variavel: >10}')

#OBS: Essa quantidade "10" também contabiliza o "ABC" da variavel "variavel". Sendo assim, 7 espaços a esquerda com mais 3 do ABC, fica igual a 10

#Print com "." para mostrar que existem espaços ao lado direito depois da variavel mensionada: 
print(f"{variavel: <10}.")

#Print centralizando os espaços:
print(f"{variavel: ^10}.")

#Utilizando limitador de exibição de digitos:
print(f"{1930.924308297:.1f}")

#Mostra a exibição do sinal "+" (caso for positivo) e "-" (caso for negativo):

#Com limitação de casas decimais:
print(f"{1930.924308297:+,.1f}")
print(f"{-1930.924308297:+,.1f}")

#Sem Limitação de casas decimais:
print(f"{1930.924308297:+}")
print(f"{-1930.924308297:+}")

#Por que isso acontece ? O python por padrão não mostra sinais quando no numero é positivo, apenas quando é negativo. Colocando um sinal de "+" deposis do ":" ele vai mensionar o sinal de "+" caso o numero for positivo. Como também o sinal de "-" se o número for negativo (Por que como já havia falado antes "Ele mostra por padrão o sinal de negativo")

print(f"O Hexadecimal de 1500 é {1500:x}")
print(f"O Hexadecimal de 1500 é {1500:>8x}")
print(f"O Hexadecimal de 1550 é {1500:<8x}.")
print(f"O Hexadecimal de 1500 é {1500:08x}")

# Utilizando o metoro "repr":
print(f"{variavel!r}")