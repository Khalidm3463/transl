from .database import Base
from sqlalchemy import Column, Integer, String

class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(String, nullable=False)
    translated_text = Column(String, nullable=False)
    target_lang = Column(String, nullable=False)
