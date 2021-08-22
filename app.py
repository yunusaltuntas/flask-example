from resource.store import Store, StoreList
from resource.item import Item, ItemList
from resource.user import UserRegister, User, UserLogin
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask import Flask
from db import db

app = Flask(__name__)
app.secret_key = 'jose'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


db.init_app(app)

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User,"/user/<int:user_id>")
api.add_resource(UserLogin,"/login")
if __name__ == '__main__':
    app.run(debug=True)
