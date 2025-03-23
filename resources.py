from flask_restful import Resource, reqparse
from models import ShortURL, db
import random
import string


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class ShortenURL(Resource):
    def post(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str, required=True, help='URL is required')
        args = parser.parse_args()

        
        original_url = args['url']
        if not original_url:
            return {'message': 'URL is required'}, 400

        
        short_code = generate_short_code()

        
        new_url = ShortURL(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()

        
        return {
            'id': new_url.id,
            'url': new_url.original_url,
            'short_code': short_code,
            'created_at': new_url.created_at.isoformat(),
            'updated_at': new_url.updated_at.isoformat()
        }, 201