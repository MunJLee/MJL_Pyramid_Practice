from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    Index
)

from sqlalchemy.orm import relationship

from .meta import Base


class Album(Base):
    __tablename__ = 'Album'
    albumId = Column('AlbumId', Integer, primary_key=True, nullable=False)
    title = Column('Title', Text, nullable=False)

    artistId = Column('ArtistId', Integer, ForeignKey('Artist.ArtistId'), nullable=False)
    creator = relationship('Artist', backref='presented_by')


Index('IFK_AlbumArtistId', Album.artistId)
