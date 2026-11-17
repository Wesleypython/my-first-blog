# Listas
'''loteria= [1,3,4,5,632,23,5,5,7345,234,]
loteria.sort()
print(loteria)
print(loteria[7:])
print(loteria[0])

loteria.append(12)
print(loteria)
loteria.pop(0)
'''

# dicionario
'''participante = {'nome': 'Wesley', 'idade': 22, 'country': 'Brasil', 'numeros':[7,22] }
print(participante['nome'])
'''

# Condições
'''nomeDaPessoa= str(input('informe o seu nome: '))
if nomeDaPessoa == 'Wesley':
    print('Autorizado')
elif nomeDaPessoa== 'Thiago':
    print('Autorizado')
else:
    print('acesso negado')'''

# Funções: Uma função é um sequência de instruções que o Python deve executar
'''def nome(name):
    print(f"Salve mano {name}")
    print("Tudo bem ?")

nome("Wesley")
'''

# Laços
# amigos = ['Jesus', 'Romario', 'Robinho', 'Thiago', 'Yago', 'Roger']

# for nome in amigos:
#     print(nome)

# for numeros in range(1,7):
#     print(numeros)

""" Curso em vídeo (módulo 3)   """
"""Explicação:"""
# lanche(pizza, suco, bolo, pudim )
# print(lanche[0:2]) #Lanche vamos mostrar os dois primeiros elementos( do 0 até o 2)

# for c in lanche:
#     print(c)

# A variável simples aqui é o "C" e a variável composta é o "lanche", para cada rodada do 
# for a variável simples vai alterar

"""Parte pratica da aula:"""

# lanche= 'Hamburguer', 'Batata', 'Suco', 'Pizza', 'Pudim' # aqui já identifica como tupla
# print(lanche[0:2]) # aqui vai printar o ('Hamburguer', 'Suco') do zero0 até o dois2
# print(lanche[-1]) # aqui vai printar o (pudim)
# print(lanche[3]) # aqui vai printar o (pudim) também
# print(lanche[-2]) # aqui vai printar o ('Pizza', 'pudim') pois é do -2 até o final

# estrutura 1
# for comida in lanche:
#     print(f'Eu comi {comida}')
# print('Eu comi bem demais')

# # Etapas da estrutura 2
# # for cont in range(0, len(lanche)):
# #     print(cont)

# # for cont in range(0, len(lanche)):
# #     print(lanche[cont])


# for cont in range(0, len(lanche)):
#     print(f'Eu comi {lanche[cont]}')

# print(sorted(lanche)) O sorted não altera a sua tupla, mas simplesmente ordena no print
# print('Eu comi bem demais novamente')

# Estrutura 3
# for indice, valor in enumerate(v):
#     print(f'Na posição {indice} encontrei valor {valor}')
# print('Final da lista')


# idade=(18, 19, 20, 21, 22)
# idade2=(22, 23, 24, 25, 26)

# somaIdades= (idade+idade2)
# print(somaIdades)
# # print(somaIdades.count(22)) # contagem do número 22
# print(somaIdades.index(18)) # localiza o número 18

"""DESAFIOS DA AULA DE TUPLA"""
# #Exercício 72 do Guanábara
# numeros= ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove',
#           'dez','onze','doze','treze','quatorze', 'quinze','dezesseis',
#           'dezessete','dezoito','dezenove','vinte')

# pesquisa= int(input('Informe um numero de 0 a 20: '))
# while True:
#     if pesquisa >= 0 and pesquisa <= 20:
#         print(f' O número digitado é: {numeros[pesquisa]}')
#         break
#     else:
#         pesquisa= int(input('Número fora da escala, informe um número entre 0 e 20: '))


"""AULA DE LISTAS"""
"""Exemplos da aula"""

# num=[1,2,3,4,5]
# # num[2] = 4
# num.append(6)
# # num.sort(reverse=True)
# # num.insert(0,7) # na posição zero insere o sete
# # num.pop(0) #Elimina o que está na posição zero
# if 6 in num:
#     num.remove(6)
# else:
#     print('Eu não encontrei o numero 6 na lista')
# print(num)


"""Aprender a programar não é velocidade, mas sim pacienciência, criatividade e prática
 - professor Guanábara"""

# v=[]
# v.append(1) 
# v.append(2) 
# v.append(3) 

# for indice, valor in enumerate(v):
#     print(f'Na posição {indice} encontrei valor {valor}')
# print('Final da lista')

# v=list()
# for cont in range(0,5):
#     v.append(input('Informe um valor: '))


# for indice, valor in enumerate(v):
#     print(f'Na posição {indice} encontrei valor {valor}')
# print('Final da lista')

# a= [2,3,4,5]
# b = a # isso não é apenas uma cópia, mas também uma ligação, assim se alterar uma altera a outra 
# b = a[:] #isso é uma cópia
 
"""EXERCÍCIOS DA AULA"""

#78 leia 5 valores, no final mostre o > eo < e seus indices

# list_five=list()
# for cont in range(0,4):
#     list_five.append(int(input('Informe o número: ')))


# for indice, l in enumerate(list_five):
#     if indice == 0:
#         menorNumero = l
#         indice_menor = indice

#         maiorNumero = l
#         indice_maior = indice


#     elif l < list_five[indice-1] and l < menorNumero:
#         menorNumero = l
#         indice_menor = indice

#     elif l > list_five[indice-1] and l > maiorNumero:
#         maiorNumero = l
#         indice_maior = indice


# print('-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*')
# print(f'O menor número é: {menorNumero} com o indice {indice_menor} ')
# print(f'O maior número é: {maiorNumero} com o indice {indice_maior}')

# OK

big_list= list()
while True:
    valida= str(input('Para inserir um valor na lista: digite (Sim): '))
    if valida.upper() in 'SIM':
        big_list.append(int(input('Informe o numero para inserir na lista: ')))
    else: 
        break

copia_lista= big_list[:]
list_par= list()
list_impar= list()
for cont in copia_lista:
    if cont % 2 == 0:
        list_par.append(cont)
    else:
        list_impar.append(cont)

print(f'A lista gerada é: {copia_lista}\n ')
print(f'A lista dos pares é: {list_par}\n ')
print(f'A lista dos impares é: {list_impar} ')











