from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(254), unique=True, index=True, nullable=False)
    phone = Column(String(32), unique=True, index=True, nullable=False)
    # Keep your original column name for compatibility
    hashed_password = Column(String(255), nullable=False)
