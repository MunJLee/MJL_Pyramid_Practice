from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class MediaType(Base):
    __tablename__ = 'MediaType'
    mediaTypeId = Column('MediaTypeId', Integer, primary_key=True, nullable=False)
    name = Column('Name', Text)
