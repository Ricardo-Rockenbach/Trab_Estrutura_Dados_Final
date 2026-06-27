import database
import menu

conexao, cursor = database.conexao()


# testar conexao:
if conexao:
    print("Conexão bem-sucedida!")

menu.menu()