from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from resource.item import Item, ItemList
from security import authenticate, identity
from resource.user import UserRegister
from db import db

app = Flask(__name__)
app.secret_key = 'jose'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app, authenticate, identity)

db.init_app(app)
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
if __name__=='__main__':

    app.run(debug=True)
