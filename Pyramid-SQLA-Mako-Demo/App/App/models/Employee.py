from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    Index
)

from sqlalchemy.orm import relationship

from .meta import Base


class Employee(Base):
    __tablename__ = 'Employee'
    employeeId = Column('EmployeeId', Integer, primary_key=True, nullable=False)
    lastName = Column('LastName', Text, nullable=False)
    firstName = Column('FirstName', Text, nullable=False)
    title = Column('Title', Text)
    birthDate = Column('BirthDate', DateTime(timezone=False))
    hireDate = Column('HireDate', DateTime(timezone=False))
    address = Column('Address', Text)
    city = Column('City', Text)
    state = Column('State', Text)
    country = Column('Country', Text)
    postalCode = Column('PostalCode', Text)
    phone = Column('Phone', Text)
    fax = Column('Fax', Text)
    email = Column('Email', Text)

    reportsTo = Column('ReportsTo', Integer, ForeignKey('Employee.EmployeeId'))
    manager = relationship('Employee', remote_side=employeeId, backref='boss')  # self-referencing foreign key


Index('IFK_EmployeeReportsTo', Employee.reportsTo)
