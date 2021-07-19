from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from item import Item, ItemList
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
if __name__=='__main__':
    app.run(debug=True)
