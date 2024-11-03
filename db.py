import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine

load_dotenv()

DATABASE_URL = (f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_password')}@{os.getenv('DB_HOST')}/"
                f"{os.getenv('DB_NAME')}")

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
