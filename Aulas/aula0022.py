# Operadores Lógicos
# and (e) or (ou) not (não)

# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira
# se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele mesmo valor
# São considerados falsy (que você ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# entrada = input('[E] - Entrar\n[S] - Sair\n\nR:')
# senha_digitada = input('Senha: ')

# senha_permitida = '1234567890'

# if ((entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida):

#     print("Você entrou no sistema")

# else:

#     print("Você saiu do sistema")

# Avaliação de curto circuito

# print(True or False)
# print(True or False or 0)
# print(0 or False or 0 or 'abc')
# print(0 or False or 0 or 'abc' or True)

# senha = 0 or False or 0 or 'abc' or True
# print(senha)

senha = input('Senha: ') or 'Sem Senha'
print(senha)
