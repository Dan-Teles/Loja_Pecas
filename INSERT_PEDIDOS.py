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
                    print("CPF não encontrado. É preciso ter cadastro para efetuar pedido.")
        
        while True:
            cod_mercadoria = input("\nDigite o código da mercadoria que deseja: ")
            
            getPRECO_query = """SELECT PRECO FROM TBL_MERCADORIAS WHERE COD_MERCADORIA = ?"""
            cursor.execute(getPRECO_query, (cod_mercadoria,))
            result = cursor.fetchone()

            if result:
                getPRECO = result[0]  
                break
            else:
                print("Código de mercadoria não cadastrado no sistema.")
                          
        
        while True:
            numero_nota_fiscal = input("\nDigite o numero da nota fiscal (apenas numeros): ")
            if len(numero_nota_fiscal) <= 100:
                break
            else:
                print("Digite nota fiscal menor que 100 caracteres!")



       
        getNomeMercadoria = """SELECT DESCRICAO_MERCADORIA FROM TBL_MERCADORIAS WHERE COD_MERCADORIA = ? """
        cursor.execute(getNomeMercadoria, (cod_mercadoria,))
        result = cursor.fetchone()

        getNome = result[0]
        while True:
           qtde = input("\nQual a quantidade de " + getNome + " que você gostaria? ")
           
           getEstoque_query = """SELECT QTD_ESTOQUE FROM TBL_MERCADORIAS WHERE COD_MERCADORIA = ?"""
           cursor.execute(getEstoque_query, (cod_mercadoria,))
           result = cursor.fetchone()

           if result:
                getEstoque = result[0]                 
                    
                #Debita pedido do estoque
                if qtde.isnumeric() and int(qtde) <= getEstoque:
                    qtdeINT = int(qtde)
                    if qtdeINT == 0:
                        print("Digite uma quantidade maior que zero.")
                        
                    else:
                        getEstoque = getEstoque - qtdeINT
                        updateEstoque = """UPDATE TBL_MERCADORIAS SET QTD_ESTOQUE = ? WHERE COD_MERCADORIA = ? """
                        cursor.execute(updateEstoque, (getEstoque, cod_mercadoria,))
                        result = cursor.fetchone()
                        break               
                else:
                    print("Quantidade de estoque insuficiente, digite um número menor. Ou caracter inserido inválido.")

        
                   
        preco_total = getPRECO * qtdeINT

        data_pedido = d.datetime.now().strftime("%x")
        hora_pedido = d.datetime.now().strftime("%X")
        
        sql = """INSERT INTO TBL_PEDIDOS
                 (ID_CLIENTE, COD_MERCADORIA, NUMERO_NOTA_FISCAL, PRECO_UNITARIO, QTDE_PEDIDOS, PRECO_TOTAL, DATA_PEDIDO, HORA_PEDIDO)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

        cursor.execute(sql, (getID, cod_mercadoria, numero_nota_fiscal, getPRECO, qtde, preco_total, data_pedido, hora_pedido))
        conector.commit()

        print("\nPedido realizado com sucesso.\n")
cursor.close()
conector.close()

print("\nFim do programa")
