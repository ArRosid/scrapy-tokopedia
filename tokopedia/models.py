from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String
)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

class Discount(Base):
    __tablename__ = "discounts"
    id = Column(Integer, primary_key=True)
    description = Column('description', String(255))
    periode = Column('periode', String(100))
    minimum_transaction = Column("minimum_transaction", String(100))
    promo_code = Column("promo_code", String(50))

    def __repr__(self):
        return f"{self.description}"