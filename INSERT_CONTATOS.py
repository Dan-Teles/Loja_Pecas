import sqlite3
import re

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
            cnpj = input("\nDigite o CNPJ do forncecedor(apenas números): ")
            if len(cnpj) == 14 and cnpj.isdigit():
                    getCOD_query = """SELECT COD_INTERNO FROM TBL_FORNECEDORES WHERE CNPJ = ?"""
                    cursor.execute(getCOD_query, (cnpj,))
                    result = cursor.fetchone()  

            if result:
                getCOD_query = result[0]  
                break
            else:
                print("CNPJ não encontrado.")
        
        
        nomeContato = input("\nDigite o nome para contato: ")
        
        while True:
            telefoneContato = input("\nDigite telefone para contato (apenas números): ")
            if len(telefoneContato) == 11 and telefoneContato.isdigit():
                break
            else:
                print("O número para contato deve conter exatamente 11 dígitos.")       


        while True:
            email = input("\nDigite o E-mail: ")
            if is_valid_email(email):
                break
            else:
                print("Não é um endereço de e-mail válido.")
        
        
        sql = """INSERT INTO TBL_CONTATOS
                 (ID_FORNECEDOR, NOME_CONTATO, TELEFONE_CONTATO, EMAIL_CONTATO)
                 VALUES (?, ?, ?, ?)"""

        cursor.execute(sql, (getCOD_query, nomeContato, telefoneContato, email))
        conector.commit()

        print("\nDados inseridos com sucesso.\n")

cursor.close()
conector.close()

print("\nFim do programa")
