from flask import Flask

from src.handlers.routes import configure_routes


def test_home_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data()
    assert response.status_code == 200


def test_login_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/login'

    response = client.get(url)
    assert response.get_data()
    assert response.status_code == 200
