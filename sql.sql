create database blog1;
use blog1;
CREATE USER 'blog1'@'localhost' IDENTIFIED BY 'blog1';
GRANT ALL PRIVILEGES ON blog1.* TO 'blog1'@'localhost' WITH GRANT OPTION;

CREATE USER 'blog1'@'%' IDENTIFIED BY 'blog1';
GRANT ALL PRIVILEGES ON blog1.* TO 'blog1'@'%' WITH GRANT OPTION;

drop table if exists blog;
drop table if exists user;


create table blog (
id int not null primary key auto_increment,
user varchar(10) not null,
blog text,
created datetime
);

insert into blog (user, blog, created) values ('aman','Hello World!!! This is a sample blog.', now());
insert into blog (user, blog, created) values ('aman','Hello World!!! This is the second blog.', now());



create table user (
id varchar(10) not null primary key,
name varchar(25),
email varchar(50),
passwd varchar(80),
salt varchar(20),
created datetime
);

