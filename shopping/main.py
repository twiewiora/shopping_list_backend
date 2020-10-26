import os

from flask import Flask
from flask_restful import Api, reqparse
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
api = Api(app)

app.config.from_object("shopping.config." + os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('amount')
parser.add_argument('user_id')

from shopping.resources import ItemList, ItemCreate, Item, ItemChangeAmount, ItemChangeBuyStatus, CategoryList

api.add_resource(ItemList, '/items')
api.add_resource(ItemCreate, '/item')
api.add_resource(Item, '/item/<item_id>')
api.add_resource(ItemChangeAmount, '/item/<item_id>/changeAmount')
api.add_resource(ItemChangeBuyStatus, '/item/<item_id>/changeBuyStatus')
api.add_resource(CategoryList, '/category/all')
