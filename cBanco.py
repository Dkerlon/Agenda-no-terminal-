import sqlite3
from sqlite3 import Error

def vincularBanco():
    caminho = "agenda/agenda.db"
    con = sqlite3.connect(caminho)
    return con
vcon = vincularBanco()

def inserir(nome,telefone,email):
    
    sql = f"""INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONE,T_EMAILCONTATO) VALUES('{nome}','{telefone}','{email}')
    """
    try:
        c = vcon.cursor()
        c.execute(sql)
        vcon.commit()
    except Error as er:
        print(er)

def consultar():
    try:
        sql = "SELECT * FROM tb_contatos"
        c = vcon.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado
    except Error as er:
        print(er)

def deletar(delete):
    sql=f"""DELETE FROM tb_contatos WHERE N_IDCONTATO={delete}"""
    try:
        c = vcon.cursor()
        c.execute(sql)
        vcon.commit()
        print("Registro removido!")
    except Error as er:
        print(er)

def update(coluna,valor,id):
    sql = f"UPDATE tb_contatos SET {coluna}='{valor}' WHERE N_IDCONTATO={id}"
    try:
        c = vcon.cursor()
        c.execute(sql)
        vcon.commit()
        print('atualizado!')
    except Error as er:
        print(er)

def consultarIdName(idName,value):
    if idName == 2:
        sql = f"SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE ?"
        c = vcon.cursor()
        c.execute(sql, (f'%{value}%',))
        resultado =c.fetchall()
        print('Sucesso!')
        return resultado
    else:
        sql = f"SELECT * FROM tb_contatos WHERE N_IDCONTATO = {value}"
        c = vcon.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado

def close():
    vcon.close()