class Funcionario():
    aumento = 1.04
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    @classmethod
    def definir_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento

#Ele tem uma relação com a classe(funcionario,dia de trabalho, dia util) mas ele nao exige
#nenhum argumento da classe. Fazer perguntas: Estou usando o argumento da classe?
    @staticmethod #Nenhum argumento da "Classe" Funcionario
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True



fabio = Funcionario('Fábio', 7000)

fabio.aplicar_aumento()
print(fabio.dados())

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()

fernando = Admin('Fernando', 14000)
fernando.atualizar_dados('Fernandinho')
print(fernando.dados())


Funcionario.definir_novo_aumento(1.05)

pedro=Funcionario('Pedro', 8000)
pedro.aplicar_aumento()
print(pedro.dados())

#metodo statico exemplo abaixo
import datetime

minha_data = datetime.date(2019, 4, 11) #quinta-feira

print(Funcionario.dia_util(minha_data))
