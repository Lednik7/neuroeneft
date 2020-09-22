from flask import jsonify
from flask_restful import reqparse, abort, Resource

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, type=str)
parser.add_argument('image', required=False, type=str)


def abort_if_date_not_found(day):
    if not advertising:
        abort(404, message=f"Advertising {day} not found")


class DateDataResource(Resource):
    def get(self, day):
        abort_if_date_not_found(day)

        return jsonify({'advertising': advertising.to_dict(
            only=('title', 'image', 'vk', 'instagram', 'site', 'telephone', 'price',
                  'text', 'id_alice_user', 'id_user', 'id_category'))})


class DateDataListResource(Resource):
    def get(self):

        return jsonify({'advertisings': [item.to_dict(
            only=('title', 'image', 'vk', 'instagram', 'site', 'telephone', 'price',
                  'text', 'id_alice_user', 'id_user', 'id_category')) for item in advertisings]})