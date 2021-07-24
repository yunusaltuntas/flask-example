from security import authenticate, identity
from resource.store import Store, StoreList
from resource.item import Item, ItemList
from resource.user import UserRegister
from flask_restful import Api
from flask_jwt import JWT
from flask import Flask
from db import db

app = Flask(__name__)
app.secret_key = 'jose'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_tables():
    db.create_all()


db.init_app(app)

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
