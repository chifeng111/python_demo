--MySQL数据的操作
主要用到insert，update，delete对应数据的插入，更新和删除

--1、创建数据库和表
create database chap3;
use chap3;

create table student(
sno char(9),
sname varchar(20),
sex char(4),
age tinyint,
depart varchar(20)
);

create table course(
cno char(2),
cname varchar(20),
cpno char(2),
credit int
);

create table sc(
sno char(9),
cno char(4),
grade double
);

show tables;
desc student;
desc course;
desc sc;

--2、插入数据
-- 插入student数据 
insert into student values
(150312101, '魏云鹏', '男', 20, '计算机'),
(150312102, '李立波', '男', 0, '计算机'),
(150312103, '牛小波', '男', 18, '机械'),
(150312104, '王美霞', '女', 19, '计算机'),
(150312105, '郭晓丽', '女', 19, '机械'),
(150312106, '陈俊峰', '男', 21, '生物');

select * from student;

--插入course数据 
insert into course values
(1, '数据库系统原理', 5, 4),
(3, '管理信息系统', 1, 4),
(4, '操作系统', 6, 3),
(5, '数据结构', 7, 4),
(7, 'C语言程序设计', 6, 4);

insert into course(cno, cname, credit) values
(2, '离散数学', 2),
(6, '数据处理技术', 2);

select * from course;

--插入成sc据 
insert into sc values
(150312101, 1, 90),
(150312101, 2, 80),
(150312101, 3, 70),
(150312101, 5, 60),
(150312101, 6, 85),
(150312101, 7, 75),
(150312102, 4, 35),
(150312102, 6, 46),
(150312102, 7, 72);

select * from sc;

--3、修改和删除数据
--修改数据
update student
set age = 19 where sno = 150312101;

update student
set age = age +1;

update student
set sex = '女' where depart = '计算机';


--删除数据
delete from student
where sno = 150312101;

delete from student
where depart = '计算机';








