import sqlite3

conector = sqlite3.connect("LojaPecas.db")

cursor = conector.cursor()

try:
	#drop table = exclui tabela
	sql = "drop table TBL_CLIENTES"
	cursor.execute(sql)
	sql = "drop table TBL_PEDIDOS"
	cursor.execute(sql)
	sql = "drop table TBL_MERCADORIAS"
	cursor.execute(sql)
	sql = "drop table TBL_FORNECEDORES"
	cursor.execute(sql)
	sql = "drop table TBL_CONTATOS"
	cursor.execute(sql)
except sqlite3.OperationalError:
	pass 

sqlClientes = """CREATE TABLE TBL_CLIENTES 
(ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,
NOME TEXT(100) NOT NULL,
RG TEXT(9) NOT NULL,
CPF TEXT(11) NOT NULL,
ENDERECO TEXT(100) NOT NULL,
EMAIL TEXT(100) NOT NULL,
TELEFONE_FIXO TEXT(10) NOT NULL,
TELEFONE_CELULAR TEXT(11))"""

cursor.execute(sqlClientes)


sqlPedidos =  """CREATE TABLE TBL_PEDIDOS
(ID_PEDIDO INTEGER PRIMARY KEY AUTOINCREMENT,
ID_CLIENTE INTEGER,
NUMERO_NOTA_FISCAL TEXT(100) NOT NULL,
PRECO_UNITARIO REAL NOT NULL,
QTDE_PEDIDOS INT NOT NULL,
PRECO_TOTAL REAL,
DATA_PEDIDO DATE,
HORA_PEDIDO TIME,
FOREIGN KEY (COD_MERCADORIA) REFERENCES TBL_MERCADORIAS(COD_MERCADORIA),
FOREIGN KEY (ID_CLIENTE) REFERENCES TBL_CLIENTES(ID_CLIENTE))"""

cursor.execute(sqlPedidos)

sqlMercadorias = """CREATE TABLE TBL_MERCADORIAS
(COD_MERCADORIA INTEGER PRIMARY KEY,
ID_FORNECEDOR INTEGER,
DESCRICAO_MERCADORIA TEXT(100) NOT NULL,
PRECO REAL NOT NULL,
QTD_ESTOQUE INTEGER NOT NULL,
FOREIGN KEY (ID_FORNECEDOR) REFERENCES TBL_FORNECEDORES(COD_INTERNO))"""

cursor.execute(sqlMercadorias)


sqlFornecedores = """CREATE TABLE TBL_FORNECEDORES
 (COD_INTERNO INTEGER PRIMARY KEY,
RAZAO_SOCIAL TEXT(100) NOT NULL,
NOME_FANTASIA TEXT(100) NOT NULL,
CNPJ TEXT(14) NOT NULL,
ENDERECO TEXT(100) NOT NULL,
TELEFONE_FORNECEDOR TEXT(11) NOT NULL)"""

cursor.execute(sqlFornecedores)


sqlContatos = """CREATE TABLE TBL_CONTATOS
 (ID_CONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
ID_FORNECEDOR INTEGER,
NOME_CONTATO TEXT(100),
TELEFONE_CONTATO INTEGER NOT NULL,
EMAIL_CONTATO TEXT(100) NOT NULL,
FOREIGN KEY (ID_FORNECEDOR) REFERENCES TBL_FORNECEDORES(COD_INTERNO))""" 

cursor.execute(sqlContatos) 


conector.commit()
cursor.close()
conector.close()


print("\nFim do programa")
               

                         

