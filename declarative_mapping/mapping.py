from typing import Any, Type
from sqlalchemy.ext.declarative import declarative_base
from engine_and_connection import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# entities
class Movies(Base):
    """
    class are the declarative mapping
    and they use declarative base
    """
    __tablename__ = 'movies'

    title: str = Column(String, primary_key=True)
    genero: str = Column(String, nullable=False)
    year: int = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Movie: {self.title} - {self.genero} - {self.year}\n"


if __name__ == '__main__':
    # Query
    data: list[Any] = session.query(Movies).all()
    print(data)
    print(data[1].title)
    # Insert
    insert: Movies = Movies(title="Scream4", genero="Horror", year=2011)
    session.add(insert)
    session.commit()
    # test
    data: list[Any] = session.query(Movies).all()
    print(data)
    # delete
    session.query(Movies).filter(Movies.title == "SpiderMan").delete()
    session.commit()
    # update
    session.query(Movies).filter(Movies.title == "Scream").update({"title": "Scream6"})
    session.commit()
