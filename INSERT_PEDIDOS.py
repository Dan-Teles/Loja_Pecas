import sqlite3
import re
import datetime as d

conector = sqlite3.connect("LojaPecas.db")
cursor = conector.cursor()

def is_valid_email(email):
    regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(regex_pattern, email):
        return True
    else:
        return False

while True:
    num = int(input("Digite 1 para inserir ou 0 para sair: "))
    
    if num == 0:
        print("\nVocê digitou 0. Saindo do programa.")
        break
    
    if num == 1:
        
        while True:
            cpf = input("\nDigite o CPF do cliente(apenas números): ")
            if len(cpf) == 11 and cpf.isdigit():
                    getID_query = """SELECT ID_CLIENTE FROM TBL_CLIENTES WHERE CPF = ?"""
                    cursor.execute(getID_query, (cpf,))
                    result = cursor.fetchone()  

            if result:
                getID = result[0]  
                break
            else:
                print("CPF não encontrado.")
        
        while True:
            cod_mercadoria = input("\nDigite o código da mercadoria: ")
            if len(cod_mercadoria) == 12 and cod_mercadoria.isdigit():
                getPRECO_query = """SELECT PRECO FROM TBL_MERCADORIAS WHERE COD_MERCADORIA = ?"""
                cursor.execute(getPRECO_query, (cod_mercadoria,))
                result = cursor.fetchone()

            if result:
                getPRECO = result[0]  
                break
            else:
                print("O Código da Mercadoria deve ter exatamente 12 números.")

        
        while True:
            numero_nota_fiscal = input("\nDigite o numero da nota fiscal(apenas numeros): ")
            if len(numero_nota_fiscal) <= 100:
                break
            else:
                print("Digite nota fiscal menor que 100 caracteres!")

        while True:
           qtde = int(input("\nDigite a quantidade dessa marcadoria: "))
           if qtde > 0:
               break
           else:
               print("Digite um número válido")


        preco_total = getPRECO * qtde

        data_pedido = d.datetime.now().strftime("%x")
        hora_pedido = d.datetime.now().strftime("%X")
        
        sql = """INSERT INTO TBL_PEDIDOS
                 (ID_CLIENTE, NUMERO_NOTA_FISCAL, PRECO_UNITARIO, QTDE_PEDIDOS, PRECO_TOTAL, DATA_PEDIDO, HORA_PEDIDO)
                 VALUES (?, ?, ?, ?, ?, ?, ?)"""

        cursor.execute(sql, (getID, numero_nota_fiscal, getPRECO, qtde, preco_total, data_pedido, hora_pedido))
        conector.commit()

        print("\nDados inseridos com sucesso.\n")
cursor.close()
conector.close()

print("\nFim do programa")
