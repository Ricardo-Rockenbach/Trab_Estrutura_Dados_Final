import os
import time
import json
from database import conexao

cursor, conexao = conexao()

def backup_json():
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    backup = {
        "categorias": categorias,
        "livros": livros
    }

    os.makedirs("backup", exist_ok=True)

    data_hora_atual = time.strftime("%Y-%m-%d_%H-%M-%S")

    with open(f"backup/backup_{data_hora_atual}.json", "w", encoding="utf-8") as arquivo:
        json.dump(backup, arquivo, indent=4, ensure_ascii=False)

    print("Backup criado com sucesso!")