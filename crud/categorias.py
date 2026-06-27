from database import conexao

cursor, conexao = conexao()

def cadastrar():
    print("Função Cadastrar categoria")
    


def listar():
    sql = "SELECT * FROM categoria"
    cursor.execute(sql)

    print("Listar categorias")
    for categoria in cursor.fetchall():
        print(f"ID: {categoria[0]}, Nome: {categoria[1]}")



def alterar():
    print("Função Alterar categoria")

def excluir():
    print("Função Excluir categoria")

