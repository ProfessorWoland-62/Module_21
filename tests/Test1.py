import pytest
from datetime import datetime


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    print('\nДо выполнения функции')
    yield
    end_time = datetime.now()
    print (f'\nПосле выполнения функции\nТест шёл: {end_time - start_time}')


@pytest.fixture()
def some_data():
    print('Наша функция выполнилась')
    return 42




def test_some_data(some_data):
    assert some_data == 42
    print('\nЭтот принт в тесте')