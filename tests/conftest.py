import pytest
from src.app import create_app
from src.models import db as _db


@pytest.fixture(scope="function")
def app():
    app = create_app({"TESTING": True,
                      "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
                      "SQLALCHEMY_TRACK_MODIFICATIONS": False})
    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()
