from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm import load_only
from pyramid.view import view_config

from .. import models


#Used as a template because SqlAlchemy/Query() does not preserve the SELECT statement column order
prefered_order = ['customerId', 'firstName', 'company', 'address', 'city', 'state', 'country', 'postalCode',
                  'phone', 'fax', 'email', 'supportRepId']


@view_config(route_name='home', renderer='../templates/homepage.mako')
def homepage(request):

    query = request.dbsession.query(models.Customer)
    columnsPresent = [key for key, value in vars(query.first()).items()]

    return {'title': 'Homepage',
            'projectname': 'Pyramid-SQLA-Mako-Demo',
            'column_labels': columnsPresent,
            'query_select': query.statement
            }


@view_config(route_name='show_customer_all', renderer='../templates/dbView.mako')
def showAllCustomers(request):
    # query the database
    query = request.dbsession.query(models.Customer)

    # check the query result and populate the relevant info accordingly
    payload = [vars(i) for i in query.all()]
    labels = list(payload[0].keys())


    return {'title': 'Show All Customers',
            'column_labels': labels,
            'query_result': payload,
            'column_pattern': prefered_order
            }


@view_config(route_name='show_customer_column', renderer='../templates/dbViewColumnOnly.mako')
def showCustomerColumn(request):

    query = request.dbsession.query(models.Customer)

    # obtain the column name to display
    targetColumn = request.matchdict['columnName']

    # check if the target column exists
    columnsPresent = [key for key, value in vars(query.first()).items()]

    if targetColumn not in columnsPresent:
        raise HTTPNotFound('NO SUCH COLUMN')
    else:
        payload = [vars(i) for i in query.options(load_only(targetColumn))]


    return {'title': 'Show a Customer Column',
            'column_labels': [targetColumn],
            'query_result': payload
            }


@view_config(route_name='show_customer_filtered_rows', renderer='../templates/dbView.mako')
def showCustomerFilteredRow(request):

    query = request.dbsession.query(models.Customer)

    # obtain the column name to display
    targetColumn = request.matchdict['columnName']

    # check if the target column exists
    columnsPresent = [key for key, value in vars(query.first()).items()]

    if targetColumn not in columnsPresent:
        raise HTTPNotFound('NO SUCH COLUMN')
    else:
        targetRow = request.matchdict['rowFilter']
        resultRows = query.filter(getattr(models.Customer, targetColumn) == targetRow).all()
        payload = [vars(i) for i in resultRows]

        return {'title': 'Show rows filtered by condition',
                'column_labels': columnsPresent,
                'query_result': payload,
                'column_pattern': prefered_order
                }

