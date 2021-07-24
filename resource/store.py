from flask_restful import Resource
from model.store import StoreModel


class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message': 'Store not found'},404
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store with name "{}" already exist.'.format(name)},400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': "an error occurred while creating the store."},500
        return store.json(),201
    def put(self,name):
        pass
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store Deleted"}
class StoreList(Resource):
    def get(self):
        return {"stores":[store.json() for store in StoreModel.query.all()]}
