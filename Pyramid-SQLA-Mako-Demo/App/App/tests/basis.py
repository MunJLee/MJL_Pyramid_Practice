import transaction
import webtest
import pytest

from pyramid import testing


class Basis:

    def setUpConnection(self):
        from ..models import get_engine, get_session_factory, get_tm_session

        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('..models')
        self.config.include('..routes')

        #session_factory = self.config.registry['dbsession_factory']
        #self.session = get_tm_session(session_factory, transaction.manager)
        #self.engine = session_factory.kw['bind']
        self.engine = get_engine(self.config.get_settings())
        session_factory = get_session_factory(self.engine)
        self.session = get_tm_session(session_factory, transaction.manager)


    def initializeDb(self):
        from ..models.meta import Base
        Base.metadata.create_all(self.engine)


    def tearDownConnection(self):
        from ..models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)


    def setUpApp(self):
        from ..models import get_engine, get_session_factory,get_tm_session
        from ..models.meta import Base
        from .. import main

        #app = main({})
        settings = {'sqlalchemy.url': 'sqlite://'}
        app = main({}, **settings)
        self.testapp = webtest.TestApp(app)

        session_factory = app.registry['dbsession_factory']
        self.session = get_tm_session(session_factory, transaction.manager)
        self.engine = session_factory.kw['bind']
        #self.engine = get_engine(self.config.get_settings())
        #session_factory = get_session_factory(self.engine)
        #self.session = get_tm_session(session_factory, transaction.manager)


        Base.metadata.create_all(bind=self.engine)

        """
        from ..models import Customer
        with transaction.manager:
            customerSample = Customer(customerId=1, firstName='Luísz(TESTONLY)', lastName='Gonçalves',
                        company='Embraer - Empresa Brasileira de Aeronáutica S.A.',
                        address='Av. Brigadeiro Faria Lima, 2170',
                        city='São José dos Campos', state='SP', country='Brazil',
                        postalCode='12227-000', phone='+55 (12) 3923-5555',
                        fax='+55 (12) 3923-5566', email='luisg@embraer.com.br',
                        supportRepId=3)

            self.session.add_all([customerSample])
        """

    def addAppData(self, dbInput):
        with transaction.manager:
            self.session.add_all(dbInput)


    def tearDownApp(self):
        from ..models.meta import Base

        Base.metadata.drop_all(bind=self.engine)
        transaction.abort()


    def createDummyRequest(dbsession):
        return testing.DummyRequest(dbsession=dbsession)


    @pytest.fixture
    def mockCustomer(self):
        from ..models import Customer

        return Customer(customerId=1, firstName='Luísz(TESTONLY)', lastName='Gonçalves',
                        company='Embraer - Empresa Brasileira de Aeronáutica S.A.',
                        address='Av. Brigadeiro Faria Lima, 2170',
                        city='São José dos Campos', state='SP', country='Brazil',
                        postalCode='12227-000', phone='+55 (12) 3923-5555',
                        fax='+55 (12) 3923-5566', email='luisg@embraer.com.br',
                        supportRepId=3)


