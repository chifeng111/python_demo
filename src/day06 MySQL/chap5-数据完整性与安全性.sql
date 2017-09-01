-- 数据完整性与安全性
完整性: 采用完整性约束条件，使其不受非法数据的影响，保证数据的一致性。
安全性: 使不受非法用户的攻击，保证数据的安全。


-- 1、主键约束完整性(注意：一个表只能有一个主键)
-- 完整性规则：
1) 主键值不能为空
2) 主键值不能重复

-- 主键约束定义
create table student(
sno char(9) primary key,
sname varchar(20),
gender char(2),
depart varchar(20)
);

或者
create table student(
sno char(9),
sname varchar(20),
gender char(2),
depart varchar(20),
primary key(sno)
);

-- 删除主键
alter table student
drop primary key;

-- 添加主键
alter table student
add primary key(sno);

-- 自增字段(注意：char不能自增长)
create table student(
sno int(9) primary key auto_increment,
sname varchar(20),
gender char(2),
depart varchar(20)
);


-- 2、外键约束完整性
-- 概念
外键约束定义了表之间的关系，主要用来维护两个表之间的一致性。

-- 外键约束定义
create table sc(
sno char(8),
cno char(4),
grade smallint,
foreign key (sno) references student (sno)
);

-- 删除外键(show create table sc;查看外键名)
alter table sc
drop foreign key 外键名;

-- 添加外键
alter table sc
add foreign key(sno) references student(sno);


-- 3、用户定义完整性
-- 非空约束(not null)
create table sc(
sno char(9),
cno char(4),
score double not null,
primary key(sno, cno)
);

-- 唯一约束(unique)
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

-- 默认约束(default)
create table student(
sno char(9) primary key,
sname varchar(20),
gender char(2),
age tinyint,
depart varchar(20) default '计算机'
);
+--------+-------------+------+-----+-----------+-------+
| Field  | Type        | Null | Key | Default   | Extra |
+--------+-------------+------+-----+-----------+-------+
| sno    | char(9)     | NO   | PRI | NULL      |       |
| sname  | varchar(20) | YES  |     | NULL      |       |
| gender | char(2)     | YES  |     | NULL      |       |
| age    | tinyint(4)  | YES  |     | NULL      |       |
| depart | varchar(20) | YES  |     | 计算机    |       |
+--------+-------------+------+-----+-----------+-------+

