-- ��ͼ����ͼ��ѯ

-- 1��������ͼ
-- һ����ʽ
create [or replace] view ��ͼ�� [(����, ����, ...)]
as ��ѯ��
[with [cascaded] check option]

-- ����ѧԺΪ��е��ѧ����ͼ
create view view_jx_student
as
select * from student
where depart = '��е';

select * from view_jx_student;

-- ����ѧ��ѡ����ͼ
create or replace view view_sc (ѧ��, ����, �γ���, �ɼ�)
as
select s.sno, s.sname, c.cname, sc.grade
from student s join course c join sc
on s.sno = sc.sno and c.cno = sc.cno;

select * from view_sc;


-- 2���鿴��ͼ
show tables;
show create view view_sc;

select * from view_sc
where �ɼ� > 70;


-- 3��ɾ����ͼ
drop view view_jx_student;


-- 4���޸���ͼ
alter view view_sc
as
��ѯ��


