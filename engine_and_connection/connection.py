from sqlalchemy import create_engine, text
from decouple import config

# the motor that specific the dialet
engine = create_engine(f"mysql+{config('DRIVER')}"
                       f"://{config('USER')}"
                       f":@{config('ADDRESS')}"
                       f":{config('PORT', cast=int)}"
                       f"/{config('DATABASE')}")
connection = engine.connect()
response = connection.execute(text("SELECT * FROM movies;"))

for row in response:
    print(row.title)


