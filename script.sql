
-- create database
create database if not exists sqlalchemy;

use sqlalchemy;

-- create a table movie

create table if not exists movies(
	title varchar(50) not null,
    genero varchar(50) not null,
    year int not null,
    primary key(title)
);


-- insert data

insert into movies(title, genero, year) values ('SpiderMan', 'Action', '2000'),
('Scream', 'Horror', 1998);

-- test
select * from movies;