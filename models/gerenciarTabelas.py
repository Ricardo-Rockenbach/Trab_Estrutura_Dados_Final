from database import conexao
import interface as ui

cursor, conexao = conexao()

def limpar():
    try:
        cursor.execute("TRUNCATE TABLE livros RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE categoria RESTART IDENTITY CASCADE")

        conexao.commit()
        ui.sucesso(" Tabelas limpas com sucesso!")

    except Exception as erro:
        conexao.rollback()
        ui.erro(f" Erro ao limpar as tabelas: {erro}")


def inserir_categorias():
    sql_insert = """
        INSERT INTO categoria (nome) VALUES
        ('Romance'),
        ('Suspense'),
        ('Ficção Científica'),
        ('Biografia'),
        ('Terror'),
        ('Fantasia'),
        ('Aventura'),
        ('História');
    """
    try:
        cursor.execute(sql_insert)
        conexao.commit()
        ui.sucesso(" Categorias inseridas com sucesso!")

    except Exception as erro:
        conexao.rollback()
        ui.erro(f" Erro ao inserir categorias: {erro}")

def inserir_livros():
    sql_insert = """
        INSERT INTO livros (titulo, autor, ano, categoriaId) VALUES
        ('Dom Casmurro', 'Machado de Assis', 1899, 1),
        ('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881, 1),
        ('Orgulho e Preconceito', 'Jane Austen', 1813, 1),
        ('Razão e Sensibilidade', 'Jane Austen', 1811, 1),
        ('Como Eu Era Antes de Você', 'Jojo Moyes', 2012, 1),
        ('A Culpa é das Estrelas', 'John Green', 2012, 1),
        ('O Morro dos Ventos Uivantes', 'Emily Brontë', 1847, 1),
        ('Anna Kariênina', 'Liev Tolstói', 1878, 1),

        ('O Código Da Vinci', 'Dan Brown', 2003, 2),
        ('Anjos e Demônios', 'Dan Brown', 2000, 2),
        ('Inferno', 'Dan Brown', 2013, 2),
        ('Garota Exemplar', 'Gillian Flynn', 2012, 2),
        ('O Silêncio dos Inocentes', 'Thomas Harris', 1988, 2),
        ('A Garota no Trem', 'Paula Hawkins', 2015, 2),
        ('O Colecionador', 'John Fowles', 1963, 2),

        ('Duna', 'Frank Herbert', 1965, 3),
        ('Messias de Duna', 'Frank Herbert', 1969, 3),
        ('Fundação', 'Isaac Asimov', 1951, 3),
        ('Fundação e Império', 'Isaac Asimov', 1952, 3),
        ('Eu, Robô', 'Isaac Asimov', 1950, 3),
        ('Neuromancer', 'William Gibson', 1984, 3),
        ('Admirável Mundo Novo', 'Aldous Huxley', 1932, 3),
        ('1984', 'George Orwell', 1949, 3),

        ('Steve Jobs', 'Walter Isaacson', 2011, 4),
        ('O Diário de Anne Frank', 'Anne Frank', 1947, 4),
        ('Longa Caminhada até a Liberdade', 'Nelson Mandela', 1994, 4),
        ('Einstein', 'Walter Isaacson', 2007, 4),
        ('Elon Musk', 'Walter Isaacson', 2023, 4),
        ('Minha História', 'Michelle Obama', 2018, 4),
        ('Eu Sou Malala', 'Malala Yousafzai', 2013, 4),

        ('It - A Coisa', 'Stephen King', 1986, 5),
        ('O Iluminado', 'Stephen King', 1977, 5),
        ('Doutor Sono', 'Stephen King', 2013, 5),
        ('Cemitério Maldito', 'Stephen King', 1983, 5),
        ('Carrie', 'Stephen King', 1974, 5),
        ('Drácula', 'Bram Stoker', 1897, 5),
        ('Frankenstein', 'Mary Shelley', 1818, 5),
        ('A Assombração da Casa da Colina', 'Shirley Jackson', 1959, 5),

        ('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997, 6),
        ('Harry Potter e a Câmara Secreta', 'J. K. Rowling', 1998, 6),
        ('Harry Potter e o Prisioneiro de Azkaban', 'J. K. Rowling', 1999, 6),
        ('Harry Potter e o Cálice de Fogo', 'J. K. Rowling', 2000, 6),
        ('O Hobbit', 'J. R. R. Tolkien', 1937, 6),
        ('A Sociedade do Anel', 'J. R. R. Tolkien', 1954, 6),
        ('As Duas Torres', 'J. R. R. Tolkien', 1954, 6),
        ('O Retorno do Rei', 'J. R. R. Tolkien', 1955, 6),

        ('A Ilha do Tesouro', 'Robert Louis Stevenson', 1883, 7),
        ('Viagem ao Centro da Terra', 'Júlio Verne', 1864, 7),
        ('Vinte Mil Léguas Submarinas', 'Júlio Verne', 1870, 7),
        ('A Volta ao Mundo em 80 Dias', 'Júlio Verne', 1872, 7),
        ('As Aventuras de Tom Sawyer', 'Mark Twain', 1876, 7),
        ('Robinson Crusoé', 'Daniel Defoe', 1719, 7),
        ('Moby Dick', 'Herman Melville', 1851, 7),

        ('Sapiens', 'Yuval Noah Harari', 2011, 8),
        ('Homo Deus', 'Yuval Noah Harari', 2015, 8),
        ('21 Lições para o Século 21', 'Yuval Noah Harari', 2018, 8),
        ('Armas, Germes e Aço', 'Jared Diamond', 1997, 8),
        ('A Segunda Guerra Mundial', 'Antony Beevor', 2012, 8),
        ('SPQR', 'Mary Beard', 2015, 8),
        ('A Era dos Extremos', 'Eric Hobsbawm', 1994, 8);
    """
    try:
        cursor.execute(sql_insert)
        conexao.commit()
        ui.sucesso(" Livros inseridos com sucesso!")

    except Exception as erro:
        conexao.rollback()
        ui.erro(f" Erro ao inserir livros: {erro}")