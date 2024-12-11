# valor1 = input("Digite um valor: ")
# valor2 = input("Digite outro valor: ")

# int_valor1 = int(valor1)
# int_valor2 = int(valor2)

# if(int_valor1 > int_valor2):
#     print(f"O primeiro valor {int_valor1} é maior que o segundo ({int_valor2})")

# else:
#     print(f"O segundo valor {int_valor2} é maior que o primeiro valor ({int_valor1})")

# # 
# # 
# # 

# valor1 = input("Digite um valor: ")
# valor2 = input("Digite outro valor: ")

# int_valor1 = int(valor1)
# int_valor2 = int(valor2)

# if(int_valor1 > int_valor2):
#     print(f"O primeiro valor {valor1} é maior que o segundo ({valor2})")

# else:
#     print(f"O segundo valor {valor2} é maior que o primeiro valor ({valor1})")

# 
#
#

v1 = input("Digite um valor: ")
v2 = input("Digite outro valor: ")

if v1 > v2:
    print("O primeiro valor é maior que o segundo")

else:
    print("O segundo valor é maior que o primeiro")

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')

else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')

# Perguntas feitas e respondidas pelo ChatGTP:

# P:

# Por que quando eu digito um valor maior (especificamente 12) no primeiro input 3 no segundo input, ele mensiona que o 3 é maior que 12.
# Porém quando mensiono um 44 no primeiro input e 3 no segundo. Ele mensiona que o 44 é maior que 3 ?
# Sendo que tanto 12 quanto 44 são maiores que 3. porém especificamente o 12 é menor que 3

# R:

# O comportamento ocorre porque, no Python, a função `input()` retorna os valores como **strings** (texto), e as comparações `>` ou `<` entre strings seguem a ordem **lexicográfica** (alfabética), e não numérica.

# ---

# ### **Explicação**

# 1. **O que está acontecendo no código?**
#    Quando você insere `12` no primeiro input e `3` no segundo, o programa está comparando as strings `"12"` e `"3"`. Na comparação de strings, o Python avalia os caracteres da esquerda para a direita, assim como ocorre com palavras em um dicionário.

#    - **Comparação lexicográfica**:  
#      Em uma comparação como `"12" > "3"`, o Python compara o primeiro caractere de cada string. O caractere `"1"` de `"12"` é menor que `"3"`, então o Python conclui que `"12"` é menor que `"3"`.

#    - Por outro lado, ao comparar `"44"` com `"3"`, o caractere `"4"` é maior que `"3"`, então o Python conclui corretamente que `"44"` é maior que `"3"`.

# 2. **Por que isso acontece com strings?**
#    Comparar strings em Python segue a tabela ASCII ou Unicode. Nesta tabela:
#    - `"1"` tem o código ASCII 49.
#    - `"3"` tem o código ASCII 51.
#    Portanto, `"1"` é menor que `"3"`, mesmo que numericamente o valor `12` (como número) seja maior que `3`.

# ---

# ### **Como corrigir isso?**
# Para que o programa funcione corretamente e realize comparações numéricas, você precisa converter as entradas de string para números, usando `int()` ou `float()`. Aqui está o código corrigido:

# ```python
# primeiro_valor = int(input('Digite um valor: '))
# segundo_valor = int(input('Digite um outro valor: '))

# if primeiro_valor > segundo_valor:
#     print(f'{primeiro_valor=} é maior do que {segundo_valor=}')
# else:
#     print(f'{segundo_valor=} é maior do que {primeiro_valor=}')
# ```

# Agora, quando você digitar `12` e `3`, o programa entenderá que `12` é maior que `3` porque estará comparando números.

# ---

# ### **Conclusão**
# O erro ocorre porque você está comparando strings (texto) em vez de números, e strings seguem regras lexicográficas, não numéricas. Sempre que precisar comparar valores numéricos, converta os inputs para números com `int()` ou `float()`.
