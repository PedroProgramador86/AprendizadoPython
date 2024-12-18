# Codigo feito:

# nome = input("Digite o seu nome: ")
# idade = input("Digite a sua idade: ")

# if(nome and idade):

#     print(f"Seu nome é {nome}")
#     print(f"Seu nome invertido é {nome[::-1]}")
#     # print(f"O seu nome contém {len(nome[" "])} espaços")
#     print(f"Seu nome tem {len(nome)} letras")
    
#     ultima_letra = len(nome)

#     print(f"A primeira letra do seu nome é {nome[0]}")
#     # print(f"A ultima letra do seu nome é {ultima_letra}")

# else:

#     print("Desculpe, você deixou campos vazios")



# Codigo Corrigido:

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if(nome and idade):

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    
    if (" " in nome): 
        
        print("O seu nome contém espaços")

    else:

        print("Seu nome não contém espaços")

    print(f"Seu nome tem {len(nome)} letras")
    
    ultima_letra = len(nome)

    print(f"A primeira letra do seu nome é {nome[0]}")
    
    print(f"A ultima letra do seu nome é {nome[-1]}")

else:

    print("Desculpe, você deixou campos vazios")
