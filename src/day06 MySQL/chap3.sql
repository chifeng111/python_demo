--MySQL���ݵĲ���
��Ҫ�õ�insert��update��delete��Ӧ���ݵĲ��룬���º�ɾ��

--1���������ݿ�ͱ�
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

--2����������
-- ����student���� 
insert into student values
(150312101, 'κ����', '��', 20, '�����'),
(150312102, '������', '��', 0, '�����'),
(150312103, 'ţС��', '��', 18, '��е'),
(150312104, '����ϼ', 'Ů', 19, '�����'),
(150312105, '������', 'Ů', 19, '��е'),
(150312106, '�¿���', '��', 21, '����');

select * from student;

--����course���� 
insert into course values
(1, '���ݿ�ϵͳԭ��', 5, 4),
(3, '������Ϣϵͳ', 1, 4),
(4, '����ϵͳ', 6, 3),
(5, '���ݽṹ', 7, 4),
(7, 'C���Գ������', 6, 4);

insert into course(cno, cname, credit) values
(2, '��ɢ��ѧ', 2),
(6, '���ݴ�����', 2);

select * from course;

--�����sc�� 
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

--3���޸ĺ�ɾ������
--�޸�����
update student
set age = 19 where sno = 150312101;

update student
set age = age +1;

update student
set sex = 'Ů' where depart = '�����';


--ɾ������
delete from student
where sno = 150312101;

delete from student
where depart = '�����';








