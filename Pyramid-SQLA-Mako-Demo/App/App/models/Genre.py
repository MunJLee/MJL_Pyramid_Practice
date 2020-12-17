from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class Genre(Base):
    __tablename__ = 'Genre'
    genreId = Column('GenreId', Integer, primary_key=True, nullable=False)
    name = Column('Name', Text)
