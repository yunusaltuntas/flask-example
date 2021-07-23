import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank!'
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name '{}' already exist ".format(name)}, 400
        data = Item.parser.parse_args()
        print(data)
        item = ItemModel(name, data["price"])
        try:
            item.insert()
        except Exception as e:
            print(e)
            return {"message": "an error accured inserting the item"}, 500
        return item.json(), 201

    def delete(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE NAME=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {"message": "Item deleted"}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data["price"])
        print(item)
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "an error accured inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "an error accured updating the item"}, 500
        return updated_item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name": row[0], "price": row[1]})
        connection.close()
        return {"items": items}
    def delete(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute('DELETE FROM items',)
        connection.commit()
        connection.close()
        return {"message": "All items delete"}


