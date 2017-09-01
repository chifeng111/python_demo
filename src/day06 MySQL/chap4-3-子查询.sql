-- 子查询
子查询是将一个查询嵌套到另一个查询中，因此又叫做嵌套查询。

-- 1、比较运算符子查询
-- 子查询返回的必须为单值 
select cno from sc
where sno = 
(select sno from student
where sname = "李立波"
);


-- 2、in子查询
-- 子查询返回的是一个集合 
select cno from sc
where sno in
(select sno from student
where depart = "机械"
);


-- 3、exists子查询
-- 子查询返回的是一个布尔值 
select sname from student
where exists
(select * from student
where gender = "男");




