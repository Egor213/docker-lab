import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env', override=True)

USER = os.getenv('USER', 'egor')
PASSWORD = os.getenv('PASSWORD', 'root123')
SERVER = os.getenv('SERVER', 'localhost')
DATABASE = os.getenv('DATABASE', 'database')
PORT = os.getenv('PORT', 5432)

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)