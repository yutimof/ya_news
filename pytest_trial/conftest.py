# conftest.py
import pytest

from engine_class import Engine
from django.test import Client
from django.contrib.auth.models import User
from news.models import Note  # Замените your_app на имя вашего приложения

@pytest.fixture(scope='session')
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    return Engine()


@pytest.fixture(autouse=True)
def start_engine(engine):
    """Фикстура запускает двигатель."""
    engine.is_running = True
    yield
    engine.is_running = False


@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def author_client(db, user):
    client = Client()
    client.force_login(user)
    return client

@pytest.fixture
def note(db, user):
    return Note.objects.create(title="Test Note", content="Test Content", author=user)

@pytest.fixture
def not_author_client(db):
    another_user = User.objects.create_user(username='anotheruser', password='password')
    client = Client()
    client.force_login(another_user)
    return client