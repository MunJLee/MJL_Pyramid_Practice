from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    Numeric,
    ForeignKey,
    Index
)

from sqlalchemy.orm import relationship

from .meta import Base


class Invoice(Base):
    __tablename__ = 'Invoice'
    invoiceId = Column('InvoiceId', Integer, primary_key=True, nullable=False)
    invoiceDate = Column('InvoiceDate', DateTime(timezone=False), nullable=False)
    billingAddress = Column('BillingAddress', Text)
    billingCity = Column('BillingCity', Text)
    billingState = Column('BillingState', Text)
    billingCountry = Column('BillingCountry', Text)
    billingPostalCode = Column('BillingPostalCode', Text)
    total = Column('Total', Numeric, nullable=False)

    customerId = Column('CustomerId', Integer, ForeignKey('Customer.CustomerId'), nullable=False)
    order = relationship('Customer', backref='purchase_order')


Index('IFK_InvoiceCustomerId', Invoice.customerId)
