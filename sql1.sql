use blog1;

drop table if exists blog;
drop table if exists user;


create table blog (
id int not null primary key auto_increment,
user varchar(10) not null,
title varchar(80),
blog text,
created TIMESTAMP
);


insert into blog (user, blog, title, created) values ('aman','Hello World!!! This is a sample blog.', 'My First Blog', now());
insert into blog (user, blog, title, created) values ('aman','Hello World!!! This is the second blog.', 'Once Again!!!', now());



create table user (
id varchar(10) not null primary key,
name varchar(25),
email varchar(50),
passwd varchar(80),
salt varchar(20),
created TIMESTAMP
);

