import mysql.connector

banco = mysql.connector.connect (
    host='localhost',
    user='root',
    passwd='',
    database='base_clientes'
)

cursor = banco.cursor()


#cursor.execute("CREATE DATABASE BASE_CLIENTES")
 
#cursor.execute("CREATE TABLE clientes(nome VARCHAR(100), documento INT(11), conta VARCHAR(8), saldo INT(10))")
def inclui_cliente_banco(nome, documento, conta, saldo): 
    comando_SQL = "INSERT INTO clientes (nome,documento,conta,saldo) VALUES (%s,%s,%s,%s)"
    dados = (nome,documento,conta,saldo) 
    cursor.execute(comando_SQL,dados) 

def exclui_cliente_banco(): 

    comando_SQL = "DELETE FROM clientes WHERE documento = '%s' "
    dados = 'vinicius'
    cursor.execute(comando_SQL,dados) 
    print(comando_SQL)


def modifica_cliente_banco(dados): 
    dados = str(input('Qual nome você quer alterar: '))
    comando = "UPDATE clientes SET nome = '" + dados + "' WHERE documento = '999966666'; "
    comando_SQL = comando
    print(comando)
    cursor.execute(comando_SQL) 
    
    