from random import randint
from dadosClientes import *

class cliente:
    def __init__(self, nome, conta, saldo = 0 ) -> None:
        self.nome = nome
        self.documento = ()
        self.conta = conta
        self.saldo = saldo

    def cadastra_cliente(self):
        self.nome = str(input('Qual seu nome completo: '))
        self.documento = str(input('Qual o numero do seu documento: '))
        self.conta = randint(00000,99999)
        self.digito = randint(0,9)
        conta = (f'{self.conta}-{self.digito}')
        self.saldo = 0
        print(f'{self.nome}, o numero da sua conta aberta é {conta}')
        inclui_cliente_banco(self.nome,self.documento, conta, self.saldo)

    '''def lista_cliente(self):
        lista_clientes = []
        cliente_conta = {'nome': self.nome, 'documento': self.documento, 'conta': (f'{self.conta}-{self.digito}'), 'saldo': self.saldo}
        lista_clientes.append(cliente_conta)
        print(lista_clientes)
    
    
        


class acao_cliente(cliente):    
    def __init__(self, nome, conta, saldo=0) -> None:
        super().__init__(nome, conta, saldo)

    def consulta_saldo(self):
        print(f'O saldo do cliente é {self.saldo}')

    def saque(self):
        valor_saque = int(input('Quanto você quer sacar? '))
        print(f'Você sacou R$ {valor_saque} da conta {self.conta}, o seu saldo agora é R$ {self.saldo - valor_saque}')
        self.saldo = self.saldo - valor_saque

    def deposito(self):
        conta = str(input('Qual o numero da sua conta: '))
        valor_deposito = int(input('Quanto você quer depositar? '))
        print(f'Você depositou R$ {valor_deposito} na conta {conta}, o seu saldo agora é R$ {self.saldo + valor_deposito}')
<<<<<<< HEAD
        self.saldo = self.saldo + valor_deposito'''


=======
        self.saldo = self.saldo + valor_deposito
>>>>>>> 1a6d0923cef10f75ccd9b2522c9a8728ddc08a52



    