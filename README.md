# SQL ALCHEMY
Studies about SQLAlchemy that is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.



### Migrations
Run:
    
    alembic init alembic

    
create a new version:

    alembic revision -m "commit"


upgrade:

    alembic upgrade head
    
downgrade:

    alembic downgrade -1

