from flask_restful import Resource

from shopping.main import db, parser
from shopping.models import ShoppingItem, Category, Product, User


class Item(Resource):
    @staticmethod
    def delete(item_id):
        try:
            item = ShoppingItem.query.filter_by(id=int(item_id)).first()
            db.session.delete(item)
            db.session.commit()
            return {'result': 'deleted'}, 204
        except Exception as e:
            return str(e)


class ItemList(Resource):
    @staticmethod
    def get(user_id):
        try:
            items = ShoppingItem.query.filter(ShoppingItem.user_id == user_id)
            result = [item.serialize() for item in items]
            result.sort(key=lambda item: (item['bought'], item['id']))
            return result
        except Exception as e:
            return str(e)


class ItemCreate(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        try:
            item = ShoppingItem(
                name=args['name'],
                amount=1,
                bought=False,
                user_id=int(args['userId'])
            )
            db.session.add(item)
            db.session.commit()
            return item.serialize(), 201
        except Exception as e:
            return str(e)


class ItemChangeAmount(Resource):
    @staticmethod
    def put(item_id):
        args = parser.parse_args()
        try:
            item = ShoppingItem.query.filter_by(id=int(item_id)).first()
            item.amount = int(args['amount'])
            db.session.commit()
            return item.serialize(), 201
        except Exception as e:
            return str(e)


class ItemChangeBuyStatus(Resource):
    @staticmethod
    def put(item_id):
        try:
            item = ShoppingItem.query.filter_by(id=int(item_id)).first()
            item.bought = not item.bought
            db.session.commit()
            return item.serialize(), 201
        except Exception as e:
            return str(e)


class CategoryList(Resource):
    @staticmethod
    def get():
        try:
            categories = Category.query.all()
            for category in categories:
                products = Product.query.filter(Product.category_id == category.id)
                category.product_list = [product.serialize() for product in products]
            return [category.serialize() for category in categories]
        except Exception as e:
            return str(e)


class UserData(Resource):
    @staticmethod
    def get(login):
        try:
            user = User.query.filter_by(login=login).first()
            if user is not None:
                return user.serialize()
            else:
                return {'desc': 'User was not found'}, 404
        except Exception as e:
            return str(e)


class WakeUp(Resource):
    @staticmethod
    def get():
        return {}
