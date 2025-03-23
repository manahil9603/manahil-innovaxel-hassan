from flask import Flask,send_from_directory
from flask_restful import Api
from flask_cors import CORS
from models import db
from resources import ShortenURL,RetrieveURL,UpdateURL,DeleteURL,URLStats
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = Flask(__name__)
CORS(app)


@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('../frontend', filename)


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)


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
    logger.info("Starting Flask application...")
    app.run(debug=True)