from cBanco import deletar,consultar,inserir,update,consultarIdName,close
from sqlite3 import Error
import re
import os

def menu():
    while True:
        try:
            menu = int(input("""1 - Inserir Novo Registro
2 - Deletar Registro
3 - Atualizar Registro
4 - Consultar ID/NOME
5 - Sair\n"""))
            if menu == 1:
                inserirRegistro()
            elif menu == 2:
                deletarRegistro()
            elif menu == 3:
                atualizarRegistro()
            elif menu == 4:
                consultarRegistros()
            elif menu == 5:
                close()
                break
            else:
                print("Opção inválida! Digite apenas números do menu")
                os.system('pause')
                limparTela()
        except ValueError as value:
            print("Opção inválida! Digite apenas números do menu")
            os.system('pause')
            limparTela()

def inserirRegistro():
    limparTela()
    nome = input('Digite seu nome e sobrenome: ').lower().strip()
    telefone = input('Digite seu telefone: ').strip()
    email = input('Digite seu email: ').strip()
    padraoEmail = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    padraoNome = r'^[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)+$'
    telefone = re.sub(r'\D','',telefone)[:11]

    if bool(re.fullmatch(padraoEmail,email)) and bool(re.fullmatch(padraoNome,nome)):
        inserir(nome,telefone,email)
    else:
        print('Você digitou algo fora do padrão')

    os.system('pause')
    limparTela()

def deletarRegistro():
    limparTela()
    resultado = consultar()
    for r in resultado:
        print(f'ID:{r[0]}, NOME:{r[1]}, TELEFONE:{r[2]}, EMAIL:{r[3]} ')
    print('------------------------------')
    try:
        delete = input('Selecione algum dos indices acima que deseja excluir\n')
        deletar(delete)
        os.system('pause')
        limparTela()
    except Error as er:
        print(er)
        os.system('pause')
        limparTela()

def atualizarRegistro():
    limparTela()
    registros = consultar()
    ids=[]
    for r in registros:
        print(f'ID:{r[0]}, NOME:{r[1]}, TELEFONE:{r[2]}, EMAIL:{r[3]} ')
    print('------------------------------')
    if len(registros) == 0:
        print('Não há registros no momento!')
        return
    try:
        id = input('Selecione algum dos indices acima que deseja atualizar\n')
        nomeTelefoneEmail=int(input(f'Deseja atualizar o 1-nome  2-telefone 3-email\n'))
        padraoEmail = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        padraoNome = r'^[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)+$'
        if nomeTelefoneEmail == 1:
            nome = input('Digite o novo nome e sobrenome: ').lower().strip()
            if bool(re.fullmatch(padraoNome,nome)):
                update("T_NOMECONTATO",nome,id)
                os.system('pause')
                limparTela()
            else:
                   print('Você digitou algo fora do padrão')
        elif nomeTelefoneEmail == 2:
            telefone = input('Digite o novo telefone: ').strip()
            telefone = re.sub(r'\D','',telefone)[:11]
            update("T_TELEFONE",telefone,id)
            os.system('pause')
            limparTela()
        elif nomeTelefoneEmail == 3:
            email = input('Digite o novo email: ').strip()
            if bool(re.fullmatch(padraoEmail,email)):
                update('T_EMAILCONTATO',email,id)
                os.system('pause')
                limparTela() 
            else:
                print('Você digitou algo fora do padrão')
    except Error as er:
        print(er)

def consultarRegistros():
    limparTela()
    consulta = input('Deseja consultar: \n1- Todos os registros\n2- Por nome\n3- Por ID\n')
    lim=5
    cont=0
    if consulta == '1':
        resultado = consultar()
        for r in resultado:
            print(f'ID:{r[0]}, NOME:{r[1]}, TELEFONE:{r[2]}, EMAIL:{r[3]} ')
            print('------------------------------')
            cont+=1
            if cont >=lim:
                cont=0
                os.system('pause')
                limparTela()
        os.system('pause')
        limparTela()
    elif consulta == '2':
        nome = input('Digite o nome que deseja consultar: ')
        resultado = consultarIdName(2,nome)
        for r in resultado:
            print(f'ID:{r[0]}, NOME:{r[1]}, TELEFONE:{r[2]}, EMAIL:{r[3]} ')
            print('------------------------------')
            cont+=1
            if cont >=lim:
                cont=0
                os.system('pause')
                limparTela()
        os.system('pause')
        limparTela()
    elif consulta == '3':
        id = input('Digite o ID que deseja consultar: ')
        resultado = consultarIdName(3,id)
        for r in resultado:
            print(f'ID:{r[0]}, NOME:{r[1]}, TELEFONE:{r[2]}, EMAIL:{r[3]} ')
            cont+=1
            print('------------------------------')
            if cont >=lim:
                cont=0
                os.system('pause')
                limparTela()
        os.system('pause')
        limparTela()
    else:
        print('Opção inválida!')
        os.system('pause')
        limparTela()
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

menu()