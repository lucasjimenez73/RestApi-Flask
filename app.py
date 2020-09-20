from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'first_store',
        'items': [
            {
                'name': 'first item of first store',
                'price': 15.99
            },
            {
                'name': 'second item of first store',
                'price': 20.99
            }
        ]
    }
]


@app.route('/api/stores')
def get_stores():
    return jsonify(stores)  # otra opcion es pasar un diccionario,flask lo convierte a json aut. {'stores':stores}


@app.route('/api/stores', methods=['POST'])
def create_store():
    body = request.get_json()
    new_store = {
        'name': body['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/api/stores/<string:name>')
def get_store(name: str):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return {'error': 404, 'message': 'Store NOT FOUND'}


@app.route('/api/stores/<string:name>/items')
def get_item_store(name: str):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return {'error': 404, 'message': 'Store NOT FOUND'}


@app.route('/api/stores/<string:name>/items', methods=['POST'])
def create_item_store(name: str):
    body = request.get_json()
    new_item = {'name': body['name'], 'price': body['price']}
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify(store)
    return {'error': 404, 'message': 'Store NOT FOUND'}


if __name__ == '__main__':
    app.run()
