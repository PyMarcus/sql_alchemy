from decouple import config
from entities import Actors, Movies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

if __name__ == '__main__':
    engine = create_engine(f"mysql+{config('DRIVER')}://{config('USER')}:@{config('ADDRESS')}:{config('PORT', cast=int)}/{config('DATABASE')}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # JOIN ACTORS AND MOVIES WHERE NAME OF MOVIE IS EQUAL
    data = session.query(Actors)\
        .join(Movies, Actors.movie_name == Movies.title)\
        .with_entities(Actors.name, Movies.title)\
            .all()
    print(data)

