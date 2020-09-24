from flask import Flask
from flask_restful import Api, reqparse, abort, Resource

app = Flask(__name__)
api = Api(app)

ITEMS = {
    'item1': {'item': 'mleko'},
    'item2': {'item': 'jajka'},
    'item3': {'item': 'bułki'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in ITEMS:
        abort(404, message="Item {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('item')


class Item(Resource):
    @staticmethod
    def get(item_id):
        abort_if_todo_doesnt_exist(item_id)
        return ITEMS[item_id]

    @staticmethod
    def delete(item_id):
        abort_if_todo_doesnt_exist(item_id)
        del ITEMS[item_id]
        return '', 204

    @staticmethod
    def put(item_id):
        args = parser.parse_args()
        task = {'item': args['item']}
        ITEMS[item_id] = task
        return task, 201


class ItemList(Resource):
    @staticmethod
    def get():
        return ITEMS

    @staticmethod
    def post():
        args = parser.parse_args()
        item_id = int(max(ITEMS.keys()).lstrip('item')) + 1
        item_id = 'item%i' % item_id
        ITEMS[item_id] = {'item': args['item']}
        return ITEMS[item_id], 201


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<item_id>')
