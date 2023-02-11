
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

-- create table actors
create table if not exists actors(
	id bigint auto_increment primary key,
	name varchar(50) not null,
    movie_name varchar(50) not null,
    foreign key(movie_name) references movies(title)
);


-- insert data

insert into movies(title, genero, year) values ('SpiderMan', 'Action', '2000'),
('Scream', 'Horror', 1998);

insert into actors(name, movie_name) values ('Sidney', 'Scream4'),
('Gale','Scream4');

-- test
select * from movies;

