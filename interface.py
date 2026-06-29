from colorama import Fore, Style, init
import os

init(autoreset=True)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def titulo(texto):
    print(Fore.CYAN + "=" * 60)
    print(Fore.WHITE + Style.BRIGHT + texto.center(60))
    print(Fore.CYAN + "=" * 60)

def sucesso(msg):
    print(Fore.GREEN + "✔ " + msg)

def erro(msg):
    print(Fore.RED + "✖ " + msg)

def aviso(msg):
    print(Fore.YELLOW + "⚠ " + msg)

def pausa():
    input("Pressione Enter para continuar...")