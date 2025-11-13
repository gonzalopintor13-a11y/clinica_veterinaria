from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DataBaseConnector:
    """Maneja la conexión a la base de datos (SQLite o MySQL)."""

    def __init__(self, db_url="sqlite:///clinica.db"):
        # Para MySQL sería: "mysql+mysqlconnector://user:password@localhost/clinica"
        self.engine = create_engine(db_url, echo=False)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()