pessoas_conhecidas = ['João', 'Maria', 'Ana', 'Fábio']
pessoa = input("Entre com o nome de uma pessoa: ")

"""if pessoa in pessoas_conhecidas:
    print("Você conhece essa pessoa")
else:
    print("Você não conhece essa pessoa")"""

"""if pessoa in pessoas_conhecidas: #concatenando com {} na frase + o .format()
    print("Você conhece {}.".format(pessoa))
else:
    print("Você não conhece {}.".format(pessoa))"""

if pessoa in pessoas_conhecidas: # forma direta de colocar a variavel atribuida
    print("Você conhece "+ pessoa)
else:
    print("Você não conhece "+ pessoa)