class cliente:
    def __init__(self,nome,conta,saldo) -> None:
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def consulta_saldo(self):
        print(f'O saldo do cliente é {self.saldo}')

    def saque(self):
        valor_saque = int(input('Quanto você quer sacar? '))
        print(f'Você sacou R$ {valor_saque} da conta {self.conta}, o seu saldo agora é R$ {self.saldo - valor_saque}')
        self.saldo = self.saldo - valor_saque

    def deposito(self):
        valor_deposito = int(input('Quanto você quer depositar? '))
        print(f'Você depositou R$ {valor_deposito} da conta {self.conta}, o seu saldo agora é R$ {self.saldo + valor_deposito}')
        self.saldo = self.saldo + valor_deposito

    

