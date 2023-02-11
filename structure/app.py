from settings import DatabaseConnectionHandler
from entities import Movies


if __name__ == '__main__':
    with DatabaseConnectionHandler() as db:
        try:
            for lines in db.session.query(Movies).all():
                print(lines)
        except Exception as e:
            db.session.rollback()
