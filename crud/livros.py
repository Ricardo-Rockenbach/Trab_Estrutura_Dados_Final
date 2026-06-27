from database import conexao

cursor, conexao = conexao()

def cadastrar():
    print("Função Cadastrar livro")


def listar():
    sql = "SELECT * FROM livro"
    cursor.execute(sql)

    print("Listar livros")
    for livro in cursor.fetchall():
        print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Categoria ID: {livro[3]}")



def alterar():
    print("Função Alterar livro")



def excluir():
    print("Função Excluir livro")

