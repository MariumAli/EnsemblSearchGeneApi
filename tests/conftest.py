import pytest

from app import db
from flask import Flask


@pytest.fixture
def app():
    """ Provides an instance of our Flask app """
    from app import create_app
    return create_app('test')


@pytest.fixture
def db():
    return db
