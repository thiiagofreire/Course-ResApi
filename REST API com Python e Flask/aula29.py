#args ==> argumentos
#kwargs ==> keyword arguments ==> argumentos de palavras-chave

def meu_metodo(arg1, arg2):
    return arg1 + arg2

print(meu_metodo(5,6))

def soma_simplificada(*args): #*args e como se fosse uma lisa mas nao precisa colocar entre colchetes.
    return sum(args)
print(soma_simplificada(6,4,5,7,3))

def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

print(metodo_kwargs(3, 'saa', 4, 'qualquer', nome='Ana', idade=25))

#args devem ser sempre antes dos kwargs
