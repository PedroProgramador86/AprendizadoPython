# Serve para printar alguma coisa de acordo com o argumento descrito entre os parenteses
print(423, 86)

#O python automaticamente faz a quebra de linha quando exibe os resultados
print(423, 86)
print(423, 86)

'''

Comando "sep" no python
Serve para criar um separador entre 2 ou mais argumentos
Sua sintaxe é:

'''

sep=""

'''
onde dentro dos parenteses pode incluir espaço ou qualquer tipo de caracter que deseja colocar entre os dois argumentos

p.ex:

'''

print(423, 86, sep="-+-")

print(423, 86, sep=" = ")

'''
OBS: Os argumentos precisam estar juntos um do outro 

Exemplo de quando o comando sep não funciona:

'''
print("Este numero {} esta separado deste {} por essa frase".format(423, 23, sep=" = "))

# Como visto o numero acima não fez a separação com o (" = ")

"""

Comando end no Python
Serve para remover a quebra de linha automatica 
Sua sintaxe é:

"""

end=''

"""
onde dentro dos parenteses pode incluir espaço ou qualquer tipo de caracter que deseja colocar entre os dois argumentos

p.ex:

"""

print(12, 23, end=' ')
print(56, 65)

# Como visto o numero acima, a quebra de linha entre o primeiro print e o segundo não ocorre. Pois o end faz essa interrupção

print(12, 23, end=' = ')
print(56, 65)

