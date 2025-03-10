from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base



# Criando a conexão com o banco SQLite
DATABASE_URL = "sqlite:///funcionarios.db"
try:
    engine = create_engine(DATABASE_URL, echo=True)
    print("Conexão com o banco de dados estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit()

# Criando a base para as classes ORM
Base = declarative_base()

# Definição da tabela Funcionarios
class Funcionario(Base):
    __tablename__ = 'Funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    cargo = Column(String(80), nullable=False)
    setor = Column(String(50), nullable=False)
    salario = Column(Float, nullable=False)
    cpf = Column(Integer, nullable=False) 
    email = Column(String(80), nullable=False)
    senha = Column(String(50), nullable=False)

# Criando a tabela no banco de dados
try:
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")
except Exception as e:
    print(f"Erro ao criar tabelas: {e}")
    exit()




