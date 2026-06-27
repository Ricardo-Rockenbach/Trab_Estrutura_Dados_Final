from database import conexao

cursor, conexao = conexao()

sql_tabela = """
CREATE TABLE IF NOT EXISTS livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(150) NOT NULL,
    ano INTEGER,
    categoriaId INTEGER,
    FOREIGN KEY (categoriaId) REFERENCES categoria(id)
)
"""

cursor.execute(sql_tabela)

sql_insert = """INSERT INTO livros (titulo, autor, ano, categoriaId) VALUES
('Clean Code', 'Robert C. Martin', 2008, 2),
('Dom Casmurro', 'Machado de Assis', 1899, 1),
('O Iluminado', 'Stephen King', 1977, 3),
('1984', 'George Orwell', 1949, 4),
('Steve Jobs', 'Walter Isaacson', 2011, 5);
"""

cursor.execute(sql_insert)

conexao.commit()