from sqlalchemy import create_engine

def get_engine():
    return create_engine("postgresql://jhan:1234@localhost:5432/retail_db")
