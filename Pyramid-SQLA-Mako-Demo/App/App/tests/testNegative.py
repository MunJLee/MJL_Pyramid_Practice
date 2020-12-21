import pytest

from .basis import Basis
from ..views import default


class TestNegativeViews(Basis):
    """Supply wrong input to the views and see if exceptions are raised"""

    def setup_method(self):
        super(TestNegativeViews, self).setUpConnection()
        self.initializeDb()

    def teardown_method(self):
        self.tearDownConnection()

    @pytest.mark.viewTesting
    @pytest.mark.parametrize("targetColumn", [
        'nonExistingName'
    ])
    def test_view_WRONGColumn(self, mockCustomer, targetColumn):
        self.session.add_all([mockCustomer])

        request = TestNegativeViews.createDummyRequest(self.session)
        request.matchdict['columnName'] = targetColumn  # route variable supplied

        with pytest.raises(Exception, match='NO SUCH COLUMN'):
            assert default.showCustomerColumn(request)


    @pytest.mark.viewTesting
    @pytest.mark.parametrize("targetColumn, rowCondition", [
        ('nonExistingName', 'nonRightValue')
    ])
    def test_view_WRONGFilteredRows(self, mockCustomer, targetColumn, rowCondition):
        self.session.add_all([mockCustomer])

        request = TestNegativeViews.createDummyRequest(self.session)
        request.matchdict['columnName'] = targetColumn
        request.matchdict['rowFilter'] = rowCondition  # row filter variable supplied

        with pytest.raises(Exception, match='NO SUCH COLUMN'):
            assert default.showCustomerFilteredRow(request)



class TestNegativeRoutes(Basis):
    """Supply wrong API URL path and see if 404 Not Found responses coming back"""

    def setup_method(self):
        super(TestNegativeRoutes, self).setUpApp()
        self.initializeDb()

    def teardown_method(self):
        self.tearDownApp()


    @pytest.mark.routeTesting
    @pytest.mark.parametrize("targetColumn", [
        'nonExistingName'
    ])
    def test_response_WRONGColumn(self, mockCustomer, targetColumn):
        TestNegativeRoutes.addAppData(self, [mockCustomer])

        targetRoute = "/Customer/" + targetColumn
        with pytest.raises(Exception, match='404 Not Found'):
            assert self.testapp.get(targetRoute)


    @pytest.mark.routeTesting
    @pytest.mark.parametrize("targetColumn, rowCondition", [
        ('nonExistingName', 'nonRightValue')
    ])
    def test_response_WRONGFilteredRows(self, mockCustomer, targetColumn, rowCondition):
        TestNegativeRoutes.addAppData(self, [mockCustomer])

        targetRoute = "/Customer/" + targetColumn + "/" + rowCondition
        with pytest.raises(Exception, match='404 Not Found'):
            assert self.testapp.get(targetRoute)
