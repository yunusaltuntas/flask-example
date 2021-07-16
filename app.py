from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'my wonderfull store',
        'items': [
            {
                'name': 'my item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods={"POST"})
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>', methods={"GET"})
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({'message': "store not found"})


@app.route('/store', methods={"GET"})
def get_stores():
    return jsonify({'store': stores})


@app.route('/store/<string:name>/items', methods={"POST"})
def create_item_in_source(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found"})


@app.route('/store/<string:name>/items', methods={"GET"})
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({'message': "store not found"})


if __name__ == '__main__':
    app.run()
