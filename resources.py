from flask_restful import Resource, reqparse
from models import ShortURL, db
from datetime import datetime
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
    
class RetrieveURL(Resource):
    def get(self, short_code):
        url_entry = ShortURL.query.filter_by(short_code=short_code).first()
        if url_entry:
            url_entry.access_count += 1
            db.session.commit()
            return {
                'id': url_entry.id,
                'url': url_entry.original_url,
                'shortCode': url_entry.short_code,
                'createdAt': url_entry.created_at.isoformat(),
                'updatedAt': url_entry.updated_at.isoformat()
            }, 200
        return {'message': 'URL not found'}, 404
    

class UpdateURL(Resource):
    def put(self, short_code):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str, required=True, help='Updated URL is required')
        args = parser.parse_args()

        url_entry = ShortURL.query.filter_by(short_code=short_code).first()
        if url_entry:
            url_entry.original_url = args['url']
            url_entry.updated_at = datetime.utcnow()
            db.session.commit()
            return {
                'id': url_entry.id,
                'url': url_entry.original_url,
                'shortCode': url_entry.short_code,
                'createdAt': url_entry.created_at.isoformat(),
                'updatedAt': url_entry.updated_at.isoformat()
            }, 200
        return {'message': 'URL not found'}, 404