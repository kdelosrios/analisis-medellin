import os 
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD= os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PORT = os.getenv("MYSQL_PORT", 3306)

engine = create_engine(
f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}",
echo=False
)

def test_connection ():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1;"))
            print("Conexión exitosa a Mysql:", result.fetchone())
    except Exception as e:
        print("Error en la conexión", e)
if __name__=="__main__":
    test_connection()
