-- �Ӳ�ѯ
�Ӳ�ѯ�ǽ�һ����ѯǶ�׵���һ����ѯ�У�����ֽ���Ƕ�ײ�ѯ��

-- 1���Ƚ�������Ӳ�ѯ
-- �Ӳ�ѯ���صı���Ϊ��ֵ 
select cno from sc
where sno = 
(select sno from student
where sname = "������"
);


-- 2��in�Ӳ�ѯ
-- �Ӳ�ѯ���ص���һ������ 
select cno from sc
where sno in
(select sno from student
where depart = "��е"
);


-- 3��exists�Ӳ�ѯ
-- �Ӳ�ѯ���ص���һ������ֵ 
select sname from student
where exists
(select * from student
where gender = "��");




