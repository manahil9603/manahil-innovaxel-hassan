from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from models import db
from resources import ShortenURL,RetrieveURL,UpdateURL,DeleteURL,URLStats

app = Flask(__name__)
CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(ShortenURL, '/shorten')
api.add_resource(RetrieveURL, '/shorten/<string:short_code>')
api.add_resource(UpdateURL, '/shorten/<string:short_code>')
api.add_resource(DeleteURL, '/shorten/<string:short_code>')
api.add_resource(URLStats, '/shorten/<string:short_code>/stats')


if __name__ == '__main__':
    app.run(debug=True)