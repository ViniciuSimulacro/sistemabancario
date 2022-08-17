import mysql.connector

banco = mysql.connector.connect (
    host='localhost',
    user='root',
    passwd='',
    database='base_clientes'
)

cursor = banco.cursor()


#cursor.execute("CREATE DATABASE BASE_CLIENTES")
 
#cursor.execute("CREATE TABLE clientes(idcliente INT(255) PRIMARY KEY , nome VARCHAR(100), documento INT(11), conta VARCHAR(8), saldo INT(10))")

def inclui_cliente_banco(nome, documento, conta, saldo): 
    comando_SQL = "INSERT INTO clientes (nome,documento,conta,saldo) VALUES (%s,%s,%s,%s)"
    dados = (nome,documento,conta,saldo) 
    cursor.execute(comando_SQL,dados) 

def exclui_cliente_banco(): 
    nome = str(input('Qual nome você quer deletar: '))
    comando = "DELETE FROM clientes WHERE nome = '" + nome + "'"
    comando_SQL = comando
    cursor.execute(comando_SQL) 
    print(comando)


def modifica_cliente_banco(): 
    dados = int(input('Qual informação você quer alterar? Digite [1]nome [2]documento: '))
    if dados == 1:
        dados = 'nome'
    if dados == 2:
        dados = 'documento'
    print(dados)
    dados_alterar = str(input(f'Qual {dados} deseja alterar: '))
    dados_alterados = str(input(f'Qual o novo {dados}: '))    

    comando = "UPDATE clientes SET " + dados + " = '" + dados_alterados + "' WHERE " + dados + " = '" + dados_alterar + "'"
    comando_SQL = comando
    
    cursor.execute(comando_SQL) 
    
    
def consulta_saldo():
    conta = str(input('Qual o numero da sua conta: '))
    comando = "SELECT * FROM clientes WHERE CONTA = '" + conta + "'"
    comando_SQL = comando
    cursor.execute(comando_SQL) 
    valores_lidos = cursor.fetchall()
    listagem = []
    for item in valores_lidos:
        listagem.append(item)
    saldo = item[4]
    print(f'O seu saldo atual é de R$ {saldo}')
    

def deposita(): 
    conta = str(input('Qual o numero da sua conta: '))
    deposito = int(input('Quanto você gostaria de depositar: '))
    comando = "SELECT * FROM clientes WHERE CONTA = '" + conta + "'"
    comando_SQL = comando
    cursor.execute(comando_SQL) 
    valores_lidos = cursor.fetchall()
    for item in valores_lidos:
        pass
    saldo = (item[4])
    print(f'O seu saldo atual é de R$ {saldo}')
    comando2 = "UPDATE clientes SET saldo = '" + str(saldo + deposito) + "' WHERE conta = '" + conta + "'"
    comando_SQL2 = comando2
    cursor.execute(comando_SQL2) 
    print(f'Você depositou R$ {deposito} na conta {conta}, agora o seu saldo é R$ {saldo + deposito}')

