import unittest
from main import app


class FlaskTest(unittest.TestCase):

    # Ensure that Flask was setup correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertIn(b'Please login', response.data)

    def test_logout(self):
        tester = app.test_client()
        response = tester.get('/logout', content_type='html/text')
        self.assertIn(b'You have been logged out of this Page! Please do re-visit', response.data)


if __name__ == "__main__":
    unittest.main()
