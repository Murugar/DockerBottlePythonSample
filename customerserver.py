from bottle import get, post, run, request, response
from json import dumps

customers = {}

@get('/customers')
def all_customers():
    response.content_type = 'application/json'
    return dumps(customers.values())

@get('/customers/<name>')
def get_customer(name=None):
    customer = customers.get(name, None)
    if customer:
        return customer
    else:
        response.status = 404
        return 'Customer {} not found.'.format(name)

@post('/customers')
def create_customer():
    customer = request.json
    name = customer['name']
    customers[name] = customer
    return {'status': 'ok'}

customers['test1'] = {'name': 'test1', 'born': 1815}

run(host='0.0.0.0', port=8888, debug=True)
