-- 连接查询

-- 1、内连接
形式一：from 表名1 [inner] join 表名2 on 表名1.列名1 = 表名2.列名2;
形式二：from 表名1, 表名2 where 表名1.列名1 = 表名2.列名2;

-- 形式一
select student.sname, sc.cno, sc.grade
from student join sc
on student.sno = sc.sno;

-- 形式二
select student.sname, sc.cno, sc.grade
from student, sc
where student.sno = sc.sno;

-- 使用别名
select s.sname, sc.cno 课程名称, sc.grade
from student s, sc
where s.sno = sc.sno;

-- 二张以上表的查询
select s.sname, c.cname, sc.grade
from student s, course c, sc
where s.sno = sc.sno and c.cno = sc.cno
order by s.sname;

select s.sname, c.cname, sc.grade
from student s join course c join sc
on s.sno = sc.sno and c.cno = sc.cno;


-- 2、外连接
左连接：查询结果包含左表中全部数据
右连接：查询结果包含右表中全部数据
形式：
from 表名1 left | right [outer] join 表名2
on 表名1.列名1 = 表名2.列名2;

select s.sname, sc.cno, sc.grade
from student s left join sc
on s.sno = sc.sno;


-- 3、复合条件连接查询
select s.sname, s.age, c.cname, sc.grade
from student s, course c, sc
where s.sno = sc.sno and c.cno = sc.cno
and s.age > 0;

select s.sname, s.age, c.cname, sc.grade
from student s join course c join sc
on s.sno = sc.sno and c.cno = sc.cno
where s.age > 0;


