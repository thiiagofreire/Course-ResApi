import functools
#decoradores tem o poder de transformar uma funcao
#Ele embrulha, mexe, altera uma função e entrega diferente
#Utiliza-se para autenticacao do usuario, para essa questao de metodo classe, estatico.

def meu_decorador(funcao):
    @functools.wraps(funcao) #wraps=embrulhar
    def func_que_roda_funcao():
        print("*****Embrulhando função no decorador!*****")
        funcao()
        print("*****Fechando embrulho*****")
    return func_que_roda_funcao

@meu_decorador
def minha_funcao():
    print("Eu sou uma função!")

print(minha_funcao())