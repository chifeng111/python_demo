--chap2:���ݶ���

--1�����ݿ�Ĳ���
show databases;

create database chap2;

alter database chap2
default characterset utf-8;

drop database chap2;


--2����Ĳ���
use chap2;
show tables;

--������
create table student(
sno char(9),
sname char(20),
gender char(2),
sage tinyint,
depart char(20)
);

--�������
alter table student
add birthday date;

--��ɾ����
alter table student
drop column birthday;

--ɾ����
drop table student;

--��������
alter table student
rename to stu;

--�޸�����
alter table stu
change gender sex char(2);

--�޸�����������
alter table stu
modify sage int;

--�޸��е�λ��
alter table stu
modify sage int after sname;

--3����������
--���Ψһ����
alter table stu
add unique index index_sname(sage);

--ɾ������
alter table stu
drop index index_sname;







