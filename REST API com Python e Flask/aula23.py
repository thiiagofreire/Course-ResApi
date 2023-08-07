#range(start,stop,step)
#start=0
#step=1

#list []
#set {}
#tuple ()

"""numeros_pares=list(range(0,20,4))
print(numeros_pares)

#for
for numero in numeros_pares:
    print(numero ** 3)"""

"""
#while --> enquanto
x=0

while x<=10:
    print(x ** 3)
    x = x+2 #incrementar para nao cair loop infinito"""

usuario_quiser = True

while usuario_quiser == True:
    usuario_input = input("Quer continuar? (S/N) ")
    if usuario_input == 'N':
        usuario_quiser = False


