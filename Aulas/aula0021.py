# Operadores Lógicos
# and (e) or (ou) not (não)

# and - Todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso, a expressão inteira será avaliada naquele mesmo valor
# São considerados falsy (que você ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# print("CONTA FLUXO_DIGITAL\n\n")

# emailc = "pedro@exemplo.com"
# senhac = "1234567890"

# email = input("Email: ")
# senha = input("Senha: ")

# confirmar_ou_sair = input("Digite:\n[E] ENTRAR\n[S] SAIR\n:")

# if(email == "pedro@exemplo.com" and senha == "1234567890" and confirmar_ou_sair == "E"):

#     print("Você entrou no sistema !")

# elif(confirmar_ou_sair == "S"):

#     print("Você saiu do sistema !")

# else:

#     print("Ops ! Algo deu errado !")

print(True and True)
print(True and True and True)
print(True and False and False)

print(bool(0))
print(bool(""))
print(bool(1))
print(bool(" "))

print(True and 0 and True)
print(True and 1 and True)
