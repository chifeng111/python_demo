-- 单表查询

-- 1、SQL一般格式
select [all | distinct] 列表达式 [, 列表达式] ...
from 表名
where 条件表达式
group by 列名 [having 条件表达式]
order by 列名 [asc | desc]
;


-- 2、列的选择
select * 
from student;

select sno, sname, gender
from student;

-- 查询计算后的列 
select sno, sname, 2017-age
from student;

-- 定义别名
select sno, sname, 2017-age 出生年份
from student;

-- 消除重复的行
select distinct depart
from student;


-- 3、行的选择
select * 
from student
where depart = '机械';

-- 比较大小
select sname, age
from student
where age < 21;

-- 确定范围
select sname, depart, age
from student
where age not between 18 and 20;

-- 确定集合
select * 
from student
where depart in ('计算机', '机械');

-- 模糊查询
select * 
from student
where sname like '李%';

select * 
from student
where sname like '李_';

-- 空值查询
select *
from student
where depart is not null;


-- 4、排序
select *
from student
order by age desc;


-- 5、聚集函数
select count(*)
from student
where depart = '机械';

select avg(age)
from student
where depart = '计算机';

select count(*), avg(age)
from student
where depart = '计算机';


-- 6、分组
select depart
from student
group by depart;

select depart, count(*)
from student
group by depart;

-- 分组和条件联合查询
select depart, count(*)
from student
group by depart having count(*) > 2;


-- 7、返回部分查询结果
select * 
from student
limit 0, 2;


-- 8、复合条件查询
select *
from student
where age > 20 and gender = '男';

