from sistema import *

cliente1 = cliente('Vinicius','3211.013.4210-0',1000.00)

print(f'O cliente {cliente1.nome} tem a conta {cliente1.conta} com o saldo de R$ {cliente1.saldo}')
cliente1.saque()
cliente1.deposito()
print(f'O cliente {cliente1.nome} tem a conta {cliente1.conta} com o saldo de R$ {cliente1.saldo}')