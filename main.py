import database
import menu
from models.gerenciarTabelas import limpar
from models.gerenciarTabelas import inserir_categorias
from models.gerenciarTabelas import inserir_livros

conexao, cursor = database.conexao()


# testar conexao:
if conexao:
    print("Conexão bem-sucedida!")

menu.menu()


# Carga inicial do banco de dados

#limpar()

# inserir_categorias()

#inserir_livros()