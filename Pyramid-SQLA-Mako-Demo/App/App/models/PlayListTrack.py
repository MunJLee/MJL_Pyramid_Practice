from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Index
)

from sqlalchemy.orm import relationship

from .meta import Base


class PlayListTrack(Base):
    __tablename__ = 'PlaylistTrack'
    playListId = Column('PlaylistId', Integer, ForeignKey('Playlist.PlaylistId'), primary_key=True, nullable=False)
    favorites = relationship('PlayList', backref='playlist_it_belongs')

    trackId = Column('TrackId', Integer, ForeignKey('Track.TrackId'), primary_key=True, nullable=False)
    trackItem = relationship('Track', backref='track_being_played')


Index('IFK_PlaylistTrackTrackId', PlayListTrack.trackId)
