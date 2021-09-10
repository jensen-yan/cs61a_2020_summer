-- 找兄弟， 父亲相同
select a.child as first, b.child as second
    from parents as a, parents as b
    where a.parent = b.parent and a.child < b.child;

-- 找祖母，孙子关系
CREATE TABLE grandparents as
    select a.parent as grandog, b.child as granpup
        from parents as a, parents as b
            where a.child = b.parent;

-- 祖母孙子毛发相同
select grandog 
    from grandparents, dogs as c, dogs as d
        where grandog = c.name and
                granpup = d.name and
                c.fur = d.fur

CREATE TABLE phrase as SELECT "hello, world" as s;
SELECT substr(s, 4, 2) || substr(s, instr(s, " ")+1, 1) from phrase;

-- create table lists as select "one" as car
