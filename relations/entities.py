from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


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


class Actors(Base):
    """
    class are the declarative mapping
    and they use declarative base
    """
    __tablename__ = 'actors'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    movie_name: str = Column(String, ForeignKey("movies.title"))

    def __repr__(self) -> str:
        return f"Actor: {self.name} - {self.movie_name}\n"
