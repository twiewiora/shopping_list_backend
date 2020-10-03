import json

from flask import Flask
from flask_restful import Api, reqparse, abort, Resource

app = Flask(__name__)
api = Api(app)
db = {'1': json.dumps({'id': '1', 'name': 'kasza', 'amount': '1', 'wasBought': 'false'}),
      '2': json.dumps({'id': '2', 'name': 'mąka', 'amount': '10', 'wasBought': 'false'}),
      '3': json.dumps({'id': '3', 'name': 'bułki', 'amount': '4', 'wasBought': 'false'})}


def abort_if_todo_doesnt_exist(item_id):
    if item_id not in db.keys():
        abort(404, message="Item {} doesn't exist".format(item_id))


parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('amount')
parser.add_argument('wasBought')


class Item(Resource):
    @staticmethod
    def delete(item_id):
        abort_if_todo_doesnt_exist(item_id)
        del db[item_id]
        return {'result': 'deleted'}, 204


class ItemList(Resource):
    @staticmethod
    def get():
        keys = db.keys()
        result = []
        for key in keys:
            result.append(json.loads(db[key]))
        return result


class ItemCreate(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        item_id = str(int(max(db.keys())) + 1)
        item_name = args['name']
        db[item_id] = json.dumps({'id': item_id, 'name': item_name, 'amount': '1', 'wasBought': 'false'})
        return json.loads(db[item_id]), 201


class ItemChangeAmount(Resource):
    @staticmethod
    def put(item_id):
        args = parser.parse_args()
        item = json.loads(db[item_id])
        item['amount'] = args['amount']
        db[item_id] = json.dumps(item)
        return json.loads(db[item_id]), 201


class ItemChangeBuyMark(Resource):
    @staticmethod
    def put(item_id):
        args = parser.parse_args()
        item = json.loads(db[item_id])
        item['wasBought'] = args['wasBought']
        db[item_id] = json.dumps(item)
        return json.loads(db[item_id]), 201


api.add_resource(ItemList, '/items')
api.add_resource(ItemCreate, '/item')
api.add_resource(Item, '/item/<item_id>')
api.add_resource(ItemChangeAmount, '/item/<item_id>/changeAmount')
api.add_resource(ItemChangeBuyMark, '/item/<item_id>/changeBuyMark')
