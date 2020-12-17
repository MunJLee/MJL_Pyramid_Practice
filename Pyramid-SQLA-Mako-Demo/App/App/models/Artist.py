from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class Artist(Base):
    __tablename__ = 'Artist'
    artistId = Column('ArtistId', Integer, primary_key=True, nullable=False)
    name = Column('Name', Text)
