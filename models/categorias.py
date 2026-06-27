from database import conexao

cursor, conexao = conexao()

sql_tabela = """
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL UNIQUE
);
"""

cursor.execute(sql_tabela)

sql_insert = """INSERT INTO categoria (nome) VALUES
('Romance'),
('Tecnologia'),
('Suspense'),
('Ficção Científica'),
('Biografia');
"""
cursor.execute(sql_insert)

conexao.commit()

