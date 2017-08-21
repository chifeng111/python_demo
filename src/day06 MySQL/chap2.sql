--chap2:数据定义

--1、数据库的操作
show databases;

create database chap2;

alter database chap2
default characterset utf-8;

drop database chap2;


--2、表的操作
use chap2;
show tables;

--创建表
create table student(
sno char(9),
sname char(20),
gender char(2),
sage tinyint,
depart char(20)
);

--表添加列
alter table student
add birthday date;

--表删除列
alter table student
drop column birthday;

--删除表
drop table student;

--表重命名
alter table student
rename to stu;

--修改列名
alter table stu
change gender sex char(2);

--修改列数据类型
alter table stu
modify sage int;

--修改列的位置
alter table stu
modify sage int after sname;

--3、索引操作
--添加唯一索引
alter table stu
add unique index index_sname(sage);

--删除索引
alter table stu
drop index index_sname;







