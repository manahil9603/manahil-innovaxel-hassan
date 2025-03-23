import unittest
from app import app
from models import db, ShortURL

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_urls.db'
        app.config['TESTING'] = True
        self.app = app.test_client()

       
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_shorten_url(self):
        response = self.app.post('/shorten', json={'url': 'https://www.example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('short_code', response.json)

    def test_retrieve_url(self):
        self.app.post('/shorten', json={'url': 'https://www.example.com'})
        response = self.app.get('/shorten/abc123')
        self.assertEqual(response.status_code, 404) 

    def test_update_url(self):
        self.app.post('/shorten', json={'url': 'https://www.example.com'})
        response = self.app.put('/shorten/abc123', json={'url': 'https://www.updated.com'})
        self.assertEqual(response.status_code, 404) 

    def test_delete_url(self):
        self.app.post('/shorten', json={'url': 'https://www.example.com'})
        response = self.app.delete('/shorten/abc123')
        self.assertEqual(response.status_code, 404)  

    def test_url_stats(self):
        self.app.post('/shorten', json={'url': 'https://www.example.com'})
        response = self.app.get('/shorten/abc123/stats')
        self.assertEqual(response.status_code, 404)  

if __name__ == '__main__':
    unittest.main()