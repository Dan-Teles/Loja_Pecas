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
        nome = input("\nDigite o nome: ")
        
        while True:
            rg = input("\nDigite o RG (apenas números): ")
            if len(rg) == 9 and rg.isdigit():
                break
            else:
                print("O RG deve ter exatamente 9 números.")       

        while True:
            cpf = input("\nDigite o CPF (apenas números): ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("O CPF deve ter exatamente 11 números.")
    
        endereco = input("\nDigite o Endereço: ")

        while True:
            email = input("\nDigite o E-mail: ")
            if is_valid_email(email):
                break
            else:
                print("Não é um endereço de e-mail válido.")

        while True:
            tel_fixo = input("\nDigite o telefone fixo (apenas números): ")
            if len(tel_fixo) == 8 and cpf.isdigit():
                break
            else:
                print("O telefone deve ter exatamente 8 números.")
        

        while True:
            tel_cel = input("\nDigite o DDD e o telefone celular (apenas números): ")
            if len(tel_cel) == 11 and cpf.isdigit():
                break
            else:
                print("O telefone deve ter exatamente 11 números.")
        
        
        sql = """INSERT INTO TBL_CLIENTES
                 (NOME, RG, CPF, ENDERECO, EMAIL, TELEFONE_FIXO, TELEFONE_CELULAR)
                 VALUES (?, ?, ?, ?, ?, ?, ?)"""

        cursor.execute(sql, (nome, rg, cpf, endereco, email, tel_fixo, tel_cel))
        conector.commit()

        print("\nDados inseridos com sucesso.\n")
cursor.close()
conector.close()

print("\nFim do programa")
