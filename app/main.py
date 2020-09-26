from flask import Flask
from flask_restful import Api, reqparse, abort, Resource

app = Flask(__name__)
api = Api(app)

ITEMS = {
    '1': {'id': '1', 'name': 'mleko', 'amount': '1', 'wasBought': 'false'},
    '2': {'id': '2', 'name': 'jajka', 'amount': '10', 'wasBought': 'false'},
    '3': {'id': '3', 'name': 'bułki', 'amount': '4', 'wasBought': 'false'}
}


def abort_if_todo_doesnt_exist(item_id):
    if item_id not in ITEMS:
        abort(404, message="Item {} doesn't exist".format(item_id))


parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('amount')
parser.add_argument('wasBought')


class Item(Resource):
    @staticmethod
    def get(item_id):
        abort_if_todo_doesnt_exist(item_id)
        return ITEMS.get(item_id)

    @staticmethod
    def delete(item_id):
        abort_if_todo_doesnt_exist(item_id)
        del ITEMS[item_id]
        return {'result': 'deleted'}, 204


class ItemList(Resource):
    @staticmethod
    def get():
        return list(ITEMS.values())


class ItemCreate(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        item_id = str(int(max(ITEMS.keys())) + 1)
        item_name = args['name']
        ITEMS[item_id] = {'id': item_id, 'name': item_name, 'amount': '1', 'wasBought': 'false'}
        return ITEMS.get(item_id), 201


class ItemChangeAmount(Resource):
    @staticmethod
    def put(item_id):
        args = parser.parse_args()
        item = ITEMS.get(item_id)
        item['amount'] = args['amount']
        return ITEMS.get(item_id), 201


class ItemChangeBuyMark(Resource):
    @staticmethod
    def put(item_id):
        args = parser.parse_args()
        item = ITEMS.get(item_id)
        item['wasBought'] = args['wasBought']
        return ITEMS.get(item_id), 201


api.add_resource(ItemList, '/items')
api.add_resource(ItemCreate, '/item')
api.add_resource(Item, '/item/<item_id>')
api.add_resource(ItemChangeAmount, '/item/<item_id>/changeAmount')
api.add_resource(ItemChangeBuyMark, '/item/<item_id>/changeBuyMark')
