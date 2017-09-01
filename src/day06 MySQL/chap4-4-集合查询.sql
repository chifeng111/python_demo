-- 集合查询
1) union: 将多个结果的行合并，并去除重复的行
2) union all: 将多个结果的行合并，保留重复的行
3) except: 返回左侧存在但右侧不存在的行的集合
4) intersect: 返回左右都存在的行的集合


-- 1、并操作
select * from student
where age >= 20
union
select * from student
where gender = '男';

-- 等价操作
select * from student
where age >= 20 or geder = '男';


-- 2、交操作(不支持了，可以用其它方法实现)
select * from student
where age >= 20
intersect
select * from student
where gender = '男';

-- 等价操作
select * from student
where age >= 20 and gender = '男';


-- 3、差操作(也不支持了)
select * from student
where age >=20
except
select * from student
where gender = '男';

-- 等价操作
select * from student
where age >= 20 and gender != '男';


