from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    Index
)

from sqlalchemy.orm import relationship

from .meta import Base


class Customer(Base):
    __tablename__ = 'Customer'
    customerId = Column('CustomerId', Integer, primary_key=True, nullable=False)
    firstName = Column('FirstName', Text, nullable=False)
    lastName = Column('LastName', Text, nullable=False)
    company = Column('Company', Text)
    address = Column('Address', Text)
    city = Column('City', Text)
    state = Column('State', Text)
    country = Column('Country', Text)
    postalCode = Column('PostalCode', Text)
    phone = Column('Phone', Text)
    fax = Column('Fax', Text)
    email = Column('Email', Text, nullable=False)

    supportRepId = Column('SupportRepId', Integer, ForeignKey('Employee.EmployeeId'))
    support = relationship('Employee', backref='support_representative')


Index('IFK_CustomerSupportRepId', Customer.supportRepId)
