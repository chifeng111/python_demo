-- �����������밲ȫ��
������: ����������Լ��������ʹ�䲻�ܷǷ����ݵ�Ӱ�죬��֤���ݵ�һ���ԡ�
��ȫ��: ʹ���ܷǷ��û��Ĺ�������֤���ݵİ�ȫ��


-- 1������Լ��������(ע�⣺һ����ֻ����һ������)
-- �����Թ���
1) ����ֵ����Ϊ��
2) ����ֵ�����ظ�

-- ����Լ������
create table student(
sno char(9) primary key,
sname varchar(20),
gender char(2),
depart varchar(20)
);

����
create table student(
sno char(9),
sname varchar(20),
gender char(2),
depart varchar(20),
primary key(sno)
);

-- ɾ������
alter table student
drop primary key;

-- �������
alter table student
add primary key(sno);

-- �����ֶ�(ע�⣺char����������)
create table student(
sno int(9) primary key auto_increment,
sname varchar(20),
gender char(2),
depart varchar(20)
);


-- 2�����Լ��������
-- ����
���Լ�������˱�֮��Ĺ�ϵ����Ҫ����ά��������֮���һ���ԡ�

-- ���Լ������
create table sc(
sno char(8),
cno char(4),
grade smallint,
foreign key (sno) references student (sno)
);

-- ɾ�����(show create table sc;�鿴�����)
alter table sc
drop foreign key �����;

-- ������
alter table sc
add foreign key(sno) references student(sno);


-- 3���û�����������
-- �ǿ�Լ��(not null)
create table sc(
sno char(9),
cno char(4),
score double not null,
primary key(sno, cno)
);

-- ΨһԼ��(unique)
create table student(
sno char(9) primary key,
sname varchar(20) unique,
gender char(2),
age tinyint,
depart varchar(20)
);
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| sno    | char(9)     | NO   | PRI | NULL    |       |
| sname  | varchar(20) | YES  | UNI | NULL    |       |
| gender | char(2)     | YES  |     | NULL    |       |
| age    | tinyint(4)  | YES  |     | NULL    |       |
| depart | varchar(20) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+

-- Ĭ��Լ��(default)
create table student(
sno char(9) primary key,
sname varchar(20),
gender char(2),
age tinyint,
depart varchar(20) default '�����'
);
+--------+-------------+------+-----+-----------+-------+
| Field  | Type        | Null | Key | Default   | Extra |
+--------+-------------+------+-----+-----------+-------+
| sno    | char(9)     | NO   | PRI | NULL      |       |
| sname  | varchar(20) | YES  |     | NULL      |       |
| gender | char(2)     | YES  |     | NULL      |       |
| age    | tinyint(4)  | YES  |     | NULL      |       |
| depart | varchar(20) | YES  |     | �����    |       |
+--------+-------------+------+-----+-----------+-------+

