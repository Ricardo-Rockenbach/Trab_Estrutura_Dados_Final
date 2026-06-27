from database import conexao

cursor, conexao = conexao()

def cadastrar():
    sql = "INSERT INTO categoria (nome) VALUES (%s)"
    nome = input("Digite o nome da categoria: ")
    cursor.execute(sql, (nome,))
    conexao.commit()

def listar():
    sql = "SELECT * FROM categoria"
    cursor.execute(sql)

    print("Listar categorias")
    for categoria in cursor.fetchall():
        print(f"ID: {categoria[0]}, Nome: {categoria[1]}")



def alterar():
    print("Alterar categoria")
    listar()

    sql = "UPDATE categoria SET nome = %s WHERE id = %s"
    id_categoria = input("Digite o ID da categoria que deseja alterar: ")
    nome = input("Digite o novo nome da categoria: ")

    cursor.execute(sql, (nome, id_categoria))
    conexao.commit()

def excluir():
    print("Excluir categoria")
    listar()
    sql = "DELETE FROM categoria WHERE id = %s"
    id_categoria = input("Digite o ID da categoria que deseja excluir: ")

    cursor.execute(sql, (id_categoria,))
    conexao.commit()
