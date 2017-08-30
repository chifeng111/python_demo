-- 视图及视图查询

-- 1、创建视图
-- 一般形式
create [or replace] view 视图名 [(列名, 列名, ...)]
as 查询句
[with [cascaded] check option]

-- 创建学院为机械的学生视图
create view view_jx_student
as
select * from student
where depart = '机械';

select * from view_jx_student;

-- 创建学生选课视图
create or replace view view_sc (学号, 姓名, 课程名, 成绩)
as
select s.sno, s.sname, c.cname, sc.grade
from student s join course c join sc
on s.sno = sc.sno and c.cno = sc.cno;

select * from view_sc;


-- 2、查看视图
show tables;
show create view view_sc;

select * from view_sc
where 成绩 > 70;


-- 3、删除视图
drop view view_jx_student;


-- 4、修改视图
alter view view_sc
as
查询句


