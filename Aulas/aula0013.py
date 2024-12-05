nome = 'Pedro Enzo Lima'
altura = 1.80
peso = 70.67
imc = peso / (altura * altura)

# f-strings (f de formatação)

linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} Kg."
linha_3 = f"Possuindo assim, o IMC de: {imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)