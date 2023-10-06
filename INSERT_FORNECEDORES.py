import sqlite3

conector = sqlite3.connect("LojaPecas.db")
cursor = conector.cursor()

while True:
    num = int(input("Digite 1 para inserir ou 0 para sair: "))
    
    if num == 0:
        print("\nVocê digitou 0. Saindo do programa.")
        break
    
    if num == 1:
        cod_interno = input("\nDigite o Código Interno: ")

        while True:
            razao_social = input("\nDigite a Razão Social: ")
            if len(razao_social) <= 100:
                break
            else:
                print("Digite uma razao social menor que 100 caracteres!")
        
        while True:
            nome_fantasia = input("\nDigite o Nome Fantasia: ")
            if len(razao_social) <= 100:
                break
            else:
                print("Digite um nome menor que 100 caracteres!")
        
        while True:
            cnpj = input("\nDigite o CPNJ:")
            if len(cnpj) == 14:
                break
            else:
                print("Digite 14 caracteres!")

        while True:
            endereco = input("\nDigite o Endereço: ")
            if len(endereco) <= 100:
                break
            else:
                print("Digite um endereco menor que 100 caracteres!")
        
        while True:
            telefone_fornecedor = input("\nDigite o telefone do Fornecedor: ")
            if len(telefone_fornecedor) <= 11:
                break
            else:
                print("Digite telefone menor de 11 caracteres!")
        
        sql = """INSERT INTO TBL_FORNECEDORES
                 (COD_INTERNO, RAZAO_SOCIAL, NOME_FANTASIA, CNPJ, ENDERECO, TELEFONE_FORNECEDOR)
                 VALUES (?, ?, ?, ?, ?, ?)"""

        cursor.execute(sql, (cod_interno, razao_social, nome_fantasia, cnpj, endereco, telefone_fornecedor))
        conector.commit()

        print("\nDados inseridos com sucesso.\n")
cursor.close()
conector.close()

print("\nFim do programa")