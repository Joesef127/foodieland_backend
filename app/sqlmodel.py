from sqlmodel import SQLModel, create_engine, Session, select, Field

DATABASE_NAME = "app.db"
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)
Base = SQLModel.metadata
Base.metadata.create_all(engine)
# Base = declarative_base()
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()