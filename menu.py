from crud import categorias as cat
from crud import livros as liv

# menu principal
def menu():
    while True:
        print("Menu:")
        print("1. Cadastrar categoria")
        print("2. Listar categorias")
        print("3. Cadastrar livro")
        print("4. Listar livros")
        print("5. Alterar livro")
        print("6. Excluir livro")
        print("7. Alterar categoria")
        print("8. Excluir categoria")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cat.cadastrar()
        elif opcao == "2":
            cat.listar()
        elif opcao == "3":
            liv.cadastrar()
        elif opcao == "4":
            liv.listar()
        elif opcao == "5":
            liv.alterar()
        elif opcao == "6":
            liv.excluir()
        elif opcao == "7":
            cat.alterar()
        elif opcao == "8":
            cat.excluir()
        elif opcao == "9":
            break
        else:
            print("Opção inválida!")