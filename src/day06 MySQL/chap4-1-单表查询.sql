-- �����ѯ

-- 1��SQLһ���ʽ
select [all | distinct] �б��ʽ [, �б��ʽ] ...
from ����
where �������ʽ
group by ���� [having �������ʽ]
order by ���� [asc | desc]
;


-- 2���е�ѡ��
select * 
from student;

select sno, sname, gender
from student;

-- ��ѯ�������� 
select sno, sname, 2017-age
from student;

-- �������
select sno, sname, 2017-age �������
from student;

-- �����ظ�����
select distinct depart
from student;


-- 3���е�ѡ��
select * 
from student
where depart = '��е';

-- �Ƚϴ�С
select sname, age
from student
where age < 21;

-- ȷ����Χ
select sname, depart, age
from student
where age not between 18 and 20;

-- ȷ������
select * 
from student
where depart in ('�����', '��е');

-- ģ����ѯ
select * 
from student
where sname like '��%';

select * 
from student
where sname like '��_';

-- ��ֵ��ѯ
select *
from student
where depart is not null;


-- 4������
select *
from student
order by age desc;


-- 5���ۼ�����
select count(*)
from student
where depart = '��е';

select avg(age)
from student
where depart = '�����';

select count(*), avg(age)
from student
where depart = '�����';


-- 6������
select depart
from student
group by depart;

select depart, count(*)
from student
group by depart;

-- ������������ϲ�ѯ
select depart, count(*)
from student
group by depart having count(*) > 2;


-- 7�����ز��ֲ�ѯ���
select * 
from student
limit 0, 2;


-- 8������������ѯ
select *
from student
where age > 20 and gender = '��';

