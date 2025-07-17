from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Connect to SQLite database (creates the file if it doesn't exist)
engine = create_engine("sqlite:///example.db", echo=True)

# 2. Base class for model definitions
Base = declarative_base()

# 3. Define a model (table)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255),unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    password = Column(String(225), nullable=False)




# 4. Create all tables
Base.metadata.create_all(engine)

# # 5. Create a session
Session = sessionmaker(bind=engine)
db = Session()
