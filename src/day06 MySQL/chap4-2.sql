-- ���Ӳ�ѯ

-- 1��������
��ʽһ��from ����1 [inner] join ����2 on ����1.����1 = ����2.����2;
��ʽ����from ����1, ����2 where ����1.����1 = ����2.����2;

-- ��ʽһ
select student.sname, sc.cno, sc.grade
from student join sc
on student.sno = sc.sno;

-- ��ʽ��
select student.sname, sc.cno, sc.grade
from student, sc
where student.sno = sc.sno;

-- ʹ�ñ���
select s.sname, sc.cno �γ�����, sc.grade
from student s, sc
where s.sno = sc.sno;

-- �������ϱ�Ĳ�ѯ
select s.sname, c.cname, sc.grade
from student s, course c, sc
where s.sno = sc.sno and c.cno = sc.cno
order by s.sname;

select s.sname, c.cname, sc.grade
from student s join course c join sc
on s.sno = sc.sno and c.cno = sc.cno;


-- 2��������
�����ӣ���ѯ������������ȫ������
�����ӣ���ѯ��������ұ���ȫ������
��ʽ��
from ����1 left | right [outer] join ����2
on ����1.����1 = ����2.����2;

select s.sname, sc.cno, sc.grade
from student s left join sc
on s.sno = sc.sno;


-- 3�������������Ӳ�ѯ
select s.sname, s.age, c.cname, sc.grade
from student s, course c, sc
where s.sno = sc.sno and c.cno = sc.cno
and s.age > 0;

select s.sname, s.age, c.cname, sc.grade
from student s join course c join sc
on s.sno = sc.sno and c.cno = sc.cno
where s.age > 0;


