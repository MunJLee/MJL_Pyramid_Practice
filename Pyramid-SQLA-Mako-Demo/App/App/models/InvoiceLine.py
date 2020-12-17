from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    ForeignKey,
    Index
)

from sqlalchemy.orm import relationship

from .meta import Base


class InvoiceLine(Base):
    __tablename__ = 'InvoiceLine'
    invoiceLineId = Column('InvoiceLineId', Integer, primary_key=True, nullable=False)
    unitPrice = Column('UnitPrice', Numeric, nullable=False)
    quantity = Column('Quantity', Integer, nullable=False)

    invoiceId = Column('InvoiceId', Integer, ForeignKey('Invoice.InvoiceId'), nullable=False)
    item = relationship('Invoice', backref='purchased_item')

    trackId = Column('TrackId', Integer, ForeignKey('Track.TrackId'), nullable=False)
    trackNum = relationship('Track', backref='track_number')


Index('IFK_InvoiceLineInvoiceId', InvoiceLine.invoiceId)

Index('IFK_InvoiceLineTrackId', InvoiceLine.trackId)
