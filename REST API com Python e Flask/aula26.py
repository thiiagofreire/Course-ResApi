#Classe é um modelo ou uma representação de um objeto
#Objeto é uma instância de uma classe

class JogadorLoteria:
    def __init__(self): # metodo padrao para instanciar um objeto quando a gente for chamar a classe criando um objeto.
        self.nome = "Pedro"
        self.numeros = (13,4,52,23,67,82)

    def total(self):
        return sum(self.numeros)

jogador_1 = JogadorLoteria()

print(jogador_1.nome)
print(jogador_1.numeros)

jogador_2 = JogadorLoteria()

print(jogador_2.total())

#Mesmo o jogador 1 quanto jogador 2 tiverem os mesmos chaves, valores são objetos diferentes