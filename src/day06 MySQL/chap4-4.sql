-- ���ϲ�ѯ
1) union: �����������кϲ�����ȥ���ظ�����
2) union all: �����������кϲ��������ظ�����
3) except: ���������ڵ��Ҳ಻���ڵ��еļ���
4) intersect: �������Ҷ����ڵ��еļ���


-- 1��������
select * from student
where age >= 20
union
select * from student
where gender = '��';

-- �ȼ۲���
select * from student
where age >= 20 or geder = '��';


-- 2��������(��֧���ˣ���������������ʵ��)
select * from student
where age >= 20
intersect
select * from student
where gender = '��';

-- �ȼ۲���
select * from student
where age >= 20 and gender = '��';


-- 3�������(Ҳ��֧����)
select * from student
where age >=20
except
select * from student
where gender = '��';

-- �ȼ۲���
select * from student
where age >= 20 and gender != '��';


