from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:89garrafasNoNavio@localhost/escola"

# Criar máquina passando o banco de dados
engine = create_engine(DATABASE_URL)

# Criar sessão e ligar ao engine
SessionLocal = sessionmaker(bind=engine)

# Criar base
Base = declarative_base()