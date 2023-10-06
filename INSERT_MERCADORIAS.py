import sqlite3

conector = sqlite3.connect("LojaPecas.db")
cursor = conector.cursor()
    
while True:
    num = int(input("Digite 1 para inserir ou 0 para sair: "))
    
    if num == 0:
        print("\nVocê digitou 0. Saindo do programa.")
        break
    
    # Realizar entrada
    if num == 1:
        while True:
            cnpj = input("\nDigite o CNPJ do FORNECEDOR: ")
            if len(cnpj) == 14:
                getCODINTERNO_query = """SELECT COD_INTERNO FROM TBL_FORNECEDORES WHERE CNPJ = ?"""
                cursor.execute(getCODINTERNO_query, (cnpj,))
                result = cursor.fetchone()  

            if result:
                getCODINTERNO = result[0]  
                break
            else:
                print("CNPJ não encontrado.")

        #Atribuindo codigo da mercadoria (tamanho max = 9; ser numero)
        while True:
            cod_mercadoria = input("\nDigite o Código da Mercadoria (apenas números): ")
            if len(cod_mercadoria) == 12 and cod_mercadoria.isdigit():
                break
            else:
                print("O Código da Mercadoria deve ter exatamente 12 números.")

        # Atribuindo descrição (text; ser menor que 100 caracteres)
        while True:
            descricao_mercadoria = input("\nDigite a Descrição da Mercadoria: ")
            if len(descricao_mercadoria) <= 100:
                break
            else:
                print("Digite uma descrição menor de 100 caracteres!")

        # Atribuindo preço (float)
        preco = float(input("\nDigite o preço da Mercadoria (apenas números): "))
            
        # Atribuindo quantidade estoque (ser numero)
        while True:
            qtd_estoque = input("\nDigite a quantidade do estoque(apenas números): ")
            if qtd_estoque.isdigit():
                break
            else:
                print("O preço deve ter apenas números!")

        # Inserindo dados na tabela mercadorias
        sql = """INSERT INTO TBL_MERCADORIAS
                 (ID_FORNECEDOR, COD_MERCADORIA, DESCRICAO_MERCADORIA, PRECO, QTD_ESTOQUE)
                 VALUES (?, ?, ?, ?, ?)"""

        cursor.execute(sql, (getCODINTERNO, cod_mercadoria, descricao_mercadoria, preco, qtd_estoque))
        conector.commit()

        print("\nDados inseridos com sucesso.\n")
cursor.close()
conector.close()

print("\nFim do programa")
