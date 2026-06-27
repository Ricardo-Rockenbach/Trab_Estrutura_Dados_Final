import psycopg2
from config import *

def conexao():

    conexao = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        sslmode=SSLMODE
    )

    cursor = conexao.cursor()
    return cursor, conexao
