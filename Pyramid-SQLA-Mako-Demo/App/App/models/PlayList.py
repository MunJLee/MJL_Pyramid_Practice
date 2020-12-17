from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class PlayList(Base):
    __tablename__ = 'Playlist'
    playListId = Column('PlaylistId', Integer, primary_key=True, nullable=False)
    name = Column('Name', Text)
