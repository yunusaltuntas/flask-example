from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item=next(filter(lamda x:x["name"]==name,items),None)
        return {"item": None},200 if item is not None else 404
    def post(self,name):
        if next(filter(lambda  x:x["name"]==name,items),None) is not None:
            return {"message":"An item with name '{}' already exist ".format(name)},400
        data = request.get_json(force=True)
        print(data)
        item = {'name': name, "price": 12.00}
        items.append(item)
        return item,201


class ItemList(Resource):
    def get(self):
        return  {"items": items}

api.add_resource(ItemList,'/items')
api.add_resource(Item, '/item/<string:name>')

app.run(debug=True)
