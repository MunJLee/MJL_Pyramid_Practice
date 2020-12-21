import pytest

from .basis import Basis
from ..views import default


class TestViews(Basis):
    """Test functions tied to the views and check if they are generating query outputs"""

    def setup_method(self):
        super(TestViews, self).setUpConnection()
        self.initializeDb()

    def teardown_method(self):
        self.tearDownConnection()


    @pytest.mark.viewTesting
    def test_view_homepage(self, mockCustomer):
        self.session.add_all([mockCustomer])

        response = default.homepage(TestViews.createDummyRequest(self.session))
        # print(response) #use pytest -s switch to check the returning output

        assert response['title'] == 'Homepage'


    @pytest.mark.viewTesting
    def test_view_showAll(self, mockCustomer):
        self.session.add_all([mockCustomer])
        response = default.showAllCustomers(TestViews.createDummyRequest(self.session))
        assert response['title'] == 'Show All Customers'


    @pytest.mark.viewTesting
    @pytest.mark.parametrize("targetColumn", [
        'lastName'
    ])
    def test_view_showColumn(self, mockCustomer, targetColumn):
        self.session.add_all([mockCustomer])

        request = TestViews.createDummyRequest(self.session)
        request.matchdict['columnName'] = targetColumn  # route variable supplied

        response = default.showCustomerColumn(request)
        assert response['title'] == 'Show a Customer Column'
        assert response['column_labels'][0] == targetColumn


    @pytest.mark.viewTesting
    @pytest.mark.parametrize("targetColumn, rowCondition", [
        ('postalCode', '12227-000')
    ])
    def test_view_showFilteredRows(self, mockCustomer, targetColumn, rowCondition):
        self.session.add_all([mockCustomer])

        request = TestViews.createDummyRequest(self.session)
        request.matchdict['columnName'] = targetColumn
        request.matchdict['rowFilter'] = rowCondition  # row filter variable supplied

        response = default.showCustomerFilteredRow(request)
        assert response['title'] == 'Show rows filtered by condition'


class TestRoutes(Basis):
    """follow the route and see if your path would load without problem (response 200)
    Also check if the resulting html page contains the identifying element"""

    def setup_method(self):
        super(TestRoutes, self).setUpApp()
        self.initializeDb()

    def teardown_method(self):
        self.tearDownApp()


    @pytest.mark.routeTesting
    def test_response_homepage(self, mockCustomer):
        TestRoutes.addAppData(self, [mockCustomer])

        response = self.testapp.get('/')
        assert response.status_code == 200
        assert response.content_type == 'text/html'
        assert '<title>Homepage</title>' in response


    @pytest.mark.routeTesting
    def test_response_showAll(self, mockCustomer):
        TestRoutes.addAppData(self, [mockCustomer])

        response = self.testapp.get('/Customer')
        assert response.status_code == 200
        assert response.content_type == 'text/html'
        assert '<title>Show All Customers</title>' in response


    @pytest.mark.routeTesting
    @pytest.mark.parametrize("targetColumn", [
        'lastName'
    ])
    def test_response_showColumn(self, mockCustomer, targetColumn):
        TestRoutes.addAppData(self, [mockCustomer])

        targetRoute = "/Customer/" + targetColumn
        response = self.testapp.get(targetRoute)
        assert response.status_code == 200
        assert response.content_type == 'text/html'
        assert '<title>Show a Customer Column</title>' in response


    @pytest.mark.routeTesting
    @pytest.mark.parametrize("targetColumn, rowCondition", [
        ('postalCode', '12227-000')
    ])
    def test_response_showFilteredRows(self, mockCustomer, targetColumn, rowCondition):
        TestRoutes.addAppData(self, [mockCustomer])

        targetRoute = "/Customer/" + targetColumn + "/" + rowCondition
        response = self.testapp.get(targetRoute)
        assert response.status_code == 200
        assert response.content_type == 'text/html'
        assert '<title>Show rows filtered by condition</title>' in response
