#from settings import DatabaseConnectionHandler
from .entities_ import Movies
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from sqlalchemy.exc import NoResultFound


# STUB -> virtual data to test
session = UnifiedAlchemyMagicMock(
    data=[
        (
            [mock.call.query(Movies),
             mock.call.filter(Movies.genero=="Teste")],
            [Movies(title='TesteFilme', genero="Teste", year=2023)]
        ),
    ]
)


def test_select():  # pytest -s -v
    global session
    try:
        response = session.query(Movies).filter(Movies.genero == "Teste").all()
        print(response)
    except NoResultFound as e:
        print(e)
