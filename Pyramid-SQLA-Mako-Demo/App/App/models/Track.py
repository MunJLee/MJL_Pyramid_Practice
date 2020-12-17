from sqlalchemy import (
    Column,
    Integer,
    Text,
    Numeric,
    ForeignKey,
    Index
)

from sqlalchemy.orm import relationship

from .meta import Base


class Track(Base):
    __tablename__ = 'Track'
    trackId = Column('TrackId', Integer, primary_key=True, nullable=False)
    name = Column('Name', Text, nullable=False)
    composer = Column('Composer', Text)
    milliseconds = Column('Milliseconds', Integer, nullable=False)
    bytes = Column('Bytes', Integer)
    unitPrice = Column('UnitPrice', Numeric, nullable=False)

    albumId = Column('AlbumId', Integer, ForeignKey('Album.AlbumId'))
    featured = relationship('Album', backref='featured_in')

    genreId = Column('GenreId', Integer, ForeignKey('Genre.GenreId'))
    style = relationship('Genre', backref='musical_genre')

    mediaTypeId = Column('MediaTypeId', Integer, ForeignKey('MediaType.MediaTypeId'), nullable=False)
    format = relationship('MediaType', backref='service_platform')


Index('IFK_TrackAlbumId', Track.albumId)

Index('IFK_TrackGenreId', Track.genreId)

Index('IFK_TrackMediaTypeId', Track.mediaTypeId)
