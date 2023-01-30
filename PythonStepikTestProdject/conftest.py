import pytest


@pytest.fixture()
def set_up():
    print(' ___!!!___Начало теста___!!!___')
    yield
    print(' ___!!!___Конец теста___!!!___')


@pytest.fixture(scope='module')
def set_group():
    print(' >>>>---Вход в систему---<<<<')
    yield
    print(' <<<<---Выход из системы--->>>>')
