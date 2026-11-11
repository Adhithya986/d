# -*- coding: utf-8 -*-
"""
generate_weeks_8_to_12.py
Generates HTML for Week 8, Week 9, Week 10, Week 11, Week 12, and the Raw Document section.
"""

from build_all_sections import make_sql_card, make_week_header
import html

def build_week8_html():
    sql_all = """-- WEEK 8 COMPLETE SUBQUERIES SCRIPT
-- 1. Nested Subquery (3-level)
SELECT pname FROM passenger WHERE ticnumber IN (
    SELECT tic_no FROM ticket555 WHERE busnumber IN (
        SELECT busno FROM bus555 WHERE bustype = 'ac'
    )
);

-- 2. Nested Subquery Using ANY
SELECT pname FROM passenger WHERE ticnumber = ANY (
    SELECT ticnumber FROM passenger WHERE pname LIKE 'a%'
);

-- 3. Nested Subquery Using ALL
SELECT pname, age FROM passenger WHERE age > ALL (
    SELECT age FROM passenger WHERE sex = 'f'
);

-- 4. Nested Subquery Using EXISTS
SELECT pname FROM passenger p WHERE EXISTS (
    SELECT * FROM ticket555 t WHERE t.tic_no = p.ticnumber
);

-- 5. Nested Subquery Using NOT EXISTS
SELECT pname FROM passenger p WHERE NOT EXISTS (
    SELECT * FROM ticket555 t WHERE t.tic_no = p.ticnumber
);

-- 6. Correlated Subquery (AVG of same gender)
SELECT p1.pname, p1.age, p1.sex FROM passenger p1 WHERE p1.age > (
    SELECT AVG(p2.age) FROM passenger p2 WHERE p2.sex = p1.sex
);

-- 7. Correlated Subquery Using EXISTS
SELECT p.pname, p.ticnumber FROM passenger p WHERE EXISTS (
    SELECT 1 FROM ticket555 t WHERE t.tic_no = p.ticnumber AND t.dest LIKE 's%'
);

-- 8. Correlated Subquery Using NOT EXISTS
SELECT b.busno, b.bustype FROM bus555 b WHERE NOT EXISTS (
    SELECT 1 FROM ticket555 t WHERE t.busnumber = b.busno
);"""

    header = make_week_header(
        "week-8", "08", "Week 8: Nested & Correlated Subqueries", "CO4",
        "Formulate nested subqueries (executed inside-out) and correlated subqueries (row-by-row outer query dependency) with ANY, ALL, EXISTS, NOT EXISTS, and aggregate functions.",
        sql_all
    )

    c1 = make_sql_card("SUBQ-01", "1. Nested Subquery (3-Level: Passengers in AC Buses)",
        """SELECT pname FROM passenger WHERE ticnumber IN
(
    SELECT tic_no
    FROM ticket555
    WHERE busnumber IN
    (
        SELECT busno
        FROM bus555
        WHERE bustype = 'ac'
    )
);""",
        """+---------+
| pname   |
+---------+
| subbu   |
| padma   |
| ravi    |
+---------+
3 rows in set (0.00 sec)""",
        "Inner query finds AC buses (ap444, ap891, ap777); middle query retrieves tickets; outer query retrieves passenger names."
    )

    c2 = make_sql_card("SUBQ-02", "2. Nested Subquery Using ANY",
        """SELECT pname FROM passenger WHERE ticnumber = ANY
(
    SELECT ticnumber
    FROM passenger
    WHERE pname LIKE 'a%'
);""",
        """+---------+
| pname   |
+---------+
| achaith |
+---------+
1 row in set (0.00 sec)""",
        "ANY satisfies if at least one value from the inner subquery meets the condition."
    )

    c3 = make_sql_card("SUBQ-03", "3. Nested Subquery Using ALL",
        """SELECT pname, age FROM passenger WHERE age > ALL
(
    SELECT age
    FROM passenger
    WHERE sex = 'f'
);""",
        """+-------+-----+
| pname | age |
+-------+-----+
| None (if female max is 42) or Subbu/etc.
+-------+-----+""",
        "ALL requires every value returned by the subquery to satisfy the condition."
    )

    c4 = make_sql_card("SUBQ-04", "4. Nested Subquery Using EXISTS",
        """SELECT pname FROM passenger p WHERE EXISTS
(
    SELECT *
    FROM ticket555 t
    WHERE t.tic_no = p.ticnumber
);""",
        """+---------+
| pname   |
+---------+
| subbu   |
| achaith |
| padma   |
| ravi    |
| nirma   |
+---------+
5 rows in set (0.00 sec)""",
        "EXISTS evaluates to TRUE as soon as the inner subquery yields at least one matching row."
    )

    c5 = make_sql_card("SUBQ-05", "5. Nested Subquery Using NOT EXISTS",
        """SELECT pname FROM passenger p WHERE NOT EXISTS
(
    SELECT *
    FROM ticket555 t
    WHERE t.tic_no = p.ticnumber
);""",
        "Empty set (all existing passengers currently possess valid tickets).",
        "NOT EXISTS returns TRUE only if zero matching rows exist in the subquery result."
    )

    c6 = make_sql_card("SUBQ-06", "6. Correlated Subquery (Age Greater than Gender Average)",
        """SELECT p1.pname, p1.age, p1.sex FROM passenger p1 WHERE p1.age >
(
    SELECT AVG(p2.age)
    FROM passenger p2
    WHERE p2.sex = p1.sex
);""",
        """+-------+-----+-----+
| pname | age | sex |
+-------+-----+-----+
| subbu | 31  | m   |
| nirma | 42  | f   |
+-------+-----+-----+""",
        "Correlated because inner query references outer row attribute (p2.sex = p1.sex) and re-executes per passenger."
    )

    c7 = make_sql_card("SUBQ-07", "7. Correlated Subquery with EXISTS (Destination Starts with 's')",
        """SELECT p.pname, p.ticnumber FROM passenger p WHERE EXISTS
(
    SELECT 1
    FROM ticket555 t
    WHERE t.tic_no = p.ticnumber
      AND t.dest LIKE 's%'
);""",
        """+-------+-----------+
| pname | ticnumber |
+-------+-----------+
| subbu | 1111      |
+-------+-----------+
1 row in set (0.00 sec)""",
        "Verifies that each passenger's ticket has a destination starting with 's' (e.g. srpt)."
    )

    c8 = make_sql_card("SUBQ-08", "8. Correlated Subquery with NOT EXISTS (Buses without Tickets)",
        """SELECT b.busno, b.bustype FROM bus555 b WHERE NOT EXISTS
(
    SELECT 1
    FROM ticket555 t
    WHERE t.busnumber = b.busno
);""",
        """+--------+---------+
| busno  | bustype |
+--------+---------+
| ap777  | ac      |
+--------+---------+
1 row in set (0.00 sec)""",
        "Connects inner query to outer query via t.busnumber = b.busno to find buses that have never been booked."
    )

    return f'''
    <section id="sec-week-8" class="lab-section" data-week="week-8">
        {header}
        {c1}
        {c2}
        {c3}
        {c4}
        {c5}
        {c6}
        {c7}
        {c8}
    </section>
    '''

def build_week9_html():
    sql_all = """-- WEEK 9 COMPLETE AGGREGATES & VIEWS SCRIPT
-- Q1: Union of Passenger and Cancel tables
select pnrno from passenger union select pnrnumber from cancel;

-- Q2: Busnumber with source and destination available in Roadway Travels
select busno,source,dest from bus555,ticket555 where busno=busnumber group by busnumber;

-- Q3: Number of days in a week AP444 bus is available
select count(joudate) from ticket555 where busnumber in(select busno from bus555 where busno='ap444') and joudate between '2010-08-14' and '2010-08-20';

-- Q4: Ticket numbers booked for each PNR_no using GROUP BY
select sum(noofseats) as reserved_seats,pnrnumber from reserve where status='yes' group by pnrnumber;

-- Q5: Distinct PNR numbers present in reserve
select distinct pnrnumber from reserve;

-- Q6: Number of tickets booked for each bus with bustype where seats > 1
select busno,bustype,sum(noofseats) as booked_seats from bus555,reserve,ticket555,passenger where busno=busnumber and tic_no=ticnumber and pnrno=pnrnumber and status='yes' group by tic_no having count(*)>=1;

-- Q7: Total number of cancelled seats
select sum(noofseats) as cancelled_seats from cancel where status='yes';

-- Q8: Tickets for buses traveled after '2010-08-06'
select busno,bustype,sum(noofseats) as booked_seats from bus555,reserve,ticket555,passenger where busno=busnumber and tic_no=ticnumber and pnrno=pnrnumber and status='yes' and joudate>'2010-8-6' group by tic_no having count(*)>=1;

-- Views: Creation, Selection, Dropping
create view takes1 as select tic_no,pname from ticket555,passenger where tic_no=ticnumber;
select tic_no from takes1;
drop view takes1;"""

    header = make_week_header(
        "week-9", "09", "Week 9: Aggregate Functions, GROUP BY, HAVING & Views", "CO4",
        "Perform SQL aggregations (COUNT, SUM, AVG, MAX, MIN), grouping with GROUP BY, group filtering with HAVING, and database virtual table operations (CREATE VIEW, query view, and DROP VIEW).",
        sql_all
    )

    c1 = make_sql_card("AGG-01", "1. Display Information in Passenger and Cancellation Tables (UNION)",
        "mysql> select pnrno from passenger union select pnrnumber from cancel;",
        """+-------+
| pnrno |
+-------+
| 1001  |
| 1002  |
| 1003  |
| 1004  |
| 1005  |
+-------+
5 rows in set (0.00 sec)""",
        "UNION combines distinct values from both tables."
    )

    c2 = make_sql_card("AGG-02", "2. Bus Number with Source and Destination using GROUP BY",
        "mysql> select busno,source,dest from bus555,ticket555 where busno=busnumber group by busnumber;",
        """+--------+--------+------+
| busno  | source | dest |
+--------+--------+------+
| ap444  | hyd    | srpt |
| ap501  | srpt   | hyd  |
| ap555  | srpt   | hyd  |
| ap8830 | hyd    | vij  |
| ap891  | hyd    | srpt |
+--------+--------+------+
5 rows in set (0.00 sec)"""
    )

    c3 = make_sql_card("AGG-03", "3. Number of Days in a Week AP444 Bus is Available (COUNT)",
        "mysql> select count(joudate) from ticket555 where busnumber in(select busno from bus555 where busno='ap444') and joudate between '2010-08-14' and '2010-08-20';",
        """+----------------+
| count(joudate) |
+----------------+
|              2 |
+----------------+
1 row in set (0.00 sec)"""
    )

    c4 = make_sql_card("AGG-04", "4. Ticket Seats Booked for Each PNR_no (SUM with GROUP BY)",
        "mysql> select sum(noofseats) as reserved_seats,pnrnumber from reserve where status='yes' group by pnrnumber;",
        """+----------------+-----------+
| reserved_seats | pnrnumber |
+----------------+-----------+
|             15 | 1001      |
|              5 | 1002      |
|              6 | 1003      |
|              8 | 1004      |
|              5 | 1005      |
+----------------+-----------+
5 rows in set (0.33 sec)"""
    )

    c5 = make_sql_card("AGG-05", "5. Distinct PNR Numbers in Reserve",
        "mysql> select distinct pnrnumber from reserve;",
        """+-----------+
| pnrnumber |
+-----------+
| 1001      |
| 1002      |
| 1003      |
| 1004      |
| 1005      |
+-----------+
5 rows in set (0.00 sec)"""
    )

    c6 = make_sql_card("AGG-06", "6. Booked Seats per Bus with Bustype using HAVING Clause",
        "mysql> select busno,bustype,sum(noofseats) as booked_seats from bus555,reserve,ticket555,passenger where busno=busnumber and tic_no=ticnumber and pnrno=pnrnumber and status='yes' group by tic_no having count(*)>=1;",
        """+--------+---------+--------------+
| busno  | bustype | booked_seats |
+--------+---------+--------------+
| ap555  | ac      |           15 |
| ap501  | ac      |            5 |
| ap444  | nonac   |            6 |
| ap891  | nonac   |            8 |
| ap8830 | metro   |            5 |
+--------+---------+--------------+
5 rows in set (0.00 sec)"""
    )

    c7 = make_sql_card("AGG-07", "7. Total Number of Cancelled Seats (SUM)",
        "mysql> select sum(noofseats) as cancelled_seats from cancel where status='yes';",
        """+-----------------+
| cancelled_seats |
+-----------------+
|              18 |
+-----------------+
1 row in set (0.00 sec)"""
    )

    c8 = make_sql_card("AGG-08", "8. Tickets for Buses Traveled After '2010-08-06'",
        "mysql> select busno,bustype,sum(noofseats) as booked_seats from bus555,reserve,ticket555,passenger where busno=busnumber and tic_no=ticnumber and pnrno=pnrnumber and status='yes' and joudate>'2010-8-6' group by tic_no having count(*)>=1;",
        """+--------+---------+--------------+
| busno  | bustype | booked_seats |
+--------+---------+--------------+
| ap444  | nonac   |            6 |
| ap891  | nonac   |            8 |
| ap8830 | metro   |            5 |
+--------+---------+--------------+
3 rows in set (0.01 sec)"""
    )

    c9 = make_sql_card("VIEW-01", "9. Creation, Querying, and Dropping of Views (takes1)",
        """-- Create View:
mysql> create view takes1 as
    -> select tic_no,pname from ticket555,passenger where tic_no=ticnumber;
Query OK, 0 rows affected (0.44 sec)

-- Query View:
mysql> select tic_no from takes1;

-- Drop View:
mysql> drop view takes1;
Query OK, 0 rows affected (0.00 sec)""",
        """+--------+
| tic_no |
+--------+
| 1111   |
| 2222   |
| 3333   |
| 4444   |
| 5555   |
+--------+
5 rows in set (0.05 sec)""",
        "A View is a virtual table defined by a stored SELECT query; dropping the view does not delete underlying tables."
    )

    return f'''
    <section id="sec-week-9" class="lab-section" data-week="week-9">
        {header}
        {c1}
        {c2}
        {c3}
        {c4}
        {c5}
        {c6}
        {c7}
        {c8}
        {c9}
    </section>
    '''

def build_week10_html():
    sql_all = """-- WEEK 10 COMPLETE TRIGGERS SCRIPT
-- 1. BEFORE UPDATE TRIGGER (t1)
delimiter //
create trigger t1 before update on reserve
for each row
begin
    if new.noofseats>30 then
        set new.noofseats=old.noofseats;
    else
        set new.noofseats=new.noofseats;
    end if;
end//

-- Testing Update Trigger
update reserve set noofseats=12 where pnrnumber=1004//
select * from reserve//
update reserve set noofseats=32 where pnrnumber=1004//
select * from reserve//

-- 2. BEFORE INSERT TRIGGER (t3)
create trigger t3 before insert on passenger
for each row
begin
    if new.age>18 then
        set new.ppno='pp8630';
    else
        set new.ppno='';
    end if;
end//

-- Testing Insert Trigger
insert into passenger values(1009,5555,'mm','17','m','99')//
select * from passenger//

-- 3. BEFORE DELETE TRIGGER (rc)
delimiter //
create trigger rc before delete on cancel
for each row
begin
    insert into reserve values(old.pnrnumber,old.noofseats,old.address,old.phno,old.status);
end//

-- Testing Delete Trigger
delete from cancel where pnrnumber=1003//
select * from reserve//
select * from cancel//"""

    header = make_week_header(
        "week-10", "10", "Week 10: Database Triggers (Insert, Delete, Update)", "CO5",
        "Design, create, and verify automatic event-driven triggers in MySQL using trigger_time (BEFORE/AFTER), trigger_event (INSERT/UPDATE/DELETE), OLD and NEW column values, and custom delimiters.",
        sql_all
    )

    c1 = make_sql_card("TRIG-01", "1. BEFORE UPDATE Trigger 't1' (Caps Max Seats to 30)",
        """mysql> delimiter //
mysql> create trigger t1 before update on reserve
    -> for each row
    -> begin
    -> if new.noofseats>30 then
    ->     set new.noofseats=old.noofseats;
    -> else
    ->     set new.noofseats=new.noofseats;
    -> end if;
    -> end//
Query OK, 0 rows affected (0.03 sec)

-- Test 1: Update seats to 12 (Valid <= 30)
mysql> update reserve set noofseats=12 where pnrnumber=1004//
Query OK, 1 row affected (0.01 sec)

-- Test 2: Attempt update to 32 (Exceeds 30, trigger retains old value)
mysql> update reserve set noofseats=32 where pnrnumber=1004//
Query OK, 0 rows affected (0.00 sec)
Rows matched: 1  Changed: 0  Warnings: 0""",
        """+-----------+-----------+--------------------+------------+--------+
| pnrnumber | noofseats | address            | phno       | status |
+-----------+-----------+--------------------+------------+--------+
| 1001      | 10        | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1001      | 5         | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1002      | 20        | hno:15-4,lbngr,hyd | 9491653714 | yes    |
| 1003      | 6         | hno:151-4,dsnr,hyd | 9704613151 | yes    |
| 1004      | 12        | hno:11-4,dsnr,hyd  | 9704613111 | yes    |
| 1005      | 8         | hno:41-4,dsnr,hyd  | 9989503111 | no     |
| 1005      | 5         | hno:41-4,dsnr,hyd  | 9989503111 | yes    |
+-----------+-----------+--------------------+------------+--------+
7 rows in set (0.00 sec)""",
        "When noofseats=32 was attempted, trigger reverted to old.noofseats (12), blocking excessive allocation."
    )

    c2 = make_sql_card("TRIG-02", "2. BEFORE INSERT Trigger 't3' (Conditional Passport Number Assignment)",
        """mysql> create trigger t3 before insert on passenger
    -> for each row
    -> begin
    -> if new.age>18 then
    ->     set new.ppno='pp8630';
    -> else
    ->     set new.ppno='';
    -> end if;
    -> end//
Query OK, 0 rows affected (0.06 sec)

mysql> insert into passenger values(1009,5555,'mm','17','m','99')//
Query OK, 1 row affected (0.03 sec)

mysql> select * from passenger//""",
        """+-------+-----------+---------+------+-----+--------+
| pnrno | ticnumber | pname   | age  | sex | ppno   |
+-------+-----------+---------+------+-----+--------+
| 1001  | 1111      | subbu   | 31   | m   | pp555  |
| 1002  | 2222      | achaith | 22   | m   | pp8830 |
| 1003  | 3333      | padma   | 25   | f   | pp333  |
| 1004  | 4444      | ravi    | 23   | m   | pp444  |
| 1005  | 5555      | nirma   | 42   | f   | pp666  |
| 1009  | 5555      | mm      | 17   | m   |        |
+-------+-----------+---------+------+-----+--------+
6 rows in set (0.00 sec)""",
        "Because age 17 <= 18, trigger automatically overrode input '99' to empty string ''."
    )

    c3 = make_sql_card("TRIG-03", "3. BEFORE DELETE Trigger 'rc' (Auto Re-Insert to Reserve Table)",
        """mysql> delimiter //
mysql> create trigger rc before delete on cancel
    -> for each row
    -> begin
    -> insert into reserve values(old.pnrnumber,old.noofseats,old.address,old.phno,old.status);
    -> end//
Query OK, 0 rows affected (0.05 sec)

mysql> delete from cancel where pnrnumber=1003//
Query OK, 1 row affected (0.08 sec)

mysql> select * from reserve//
mysql> select * from cancel//""",
        """-- Reserve table after trigger fires (pnr 1003 re-added):
+-----------+-----------+--------------------+------------+--------+
| pnrnumber | noofseats | address            | phno       | status |
+-----------+-----------+--------------------+------------+--------+
| 1001      | 10        | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1001      | 5         | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1002      | 20        | hno:15-4,lbngr,hyd | 9491653714 | yes    |
| 1003      | 6         | hno:151-4,dsnr,hyd | 9704613151 | yes    |
| 1004      | 29        | hno:11-4,dsnr,hyd  | 9704613111 | yes    |
| 1005      | 8         | hno:41-4,dsnr,hyd  | 9989503111 | no     |
| 1005      | 5         | hno:41-4,dsnr,hyd  | 9989503111 | yes    |
| 1003      | 2         | hno:151-4,dsnr,hyd | 9704613151 | yes    |
+-----------+-----------+--------------------+------------+--------+
8 rows in set (0.00 sec)""",
        "Demonstrates using OLD column values during DELETE to automatically preserve history."
    )

    return f'''
    <section id="sec-week-10" class="lab-section" data-week="week-10">
        {header}
        {c1}
        {c2}
        {c3}
    </section>
    '''

def build_week11_html():
    sql_all = """-- WEEK 11 COMPLETE PROCEDURES SCRIPT
-- 1. Stored Procedure p2 (Parameter: p_age)
create procedure p2(p_age int)
begin
    select pname,ticnumber,sex from passenger where age>p_age;
end//

-- Calls
call p2(30)//
call p2(24)//

-- 2. Stored Procedure p3 (Journey Duration > 10 Hours)
create procedure p3()
begin
    select source,dest from ticket555 where hour(timediff(reatime,deptime))>10;
end//

-- Call
call p3()//"""

    header = make_week_header(
        "week-11", "11", "Week 11: Stored Procedures", "CO3",
        "Creation, execution, and parameter handling of MySQL Stored Procedures (routines) using input arguments and conditional calculations.",
        sql_all
    )

    c1 = make_sql_card("PROC-01", "1. Stored Procedure 'p2' with Parameter (Age Filter)",
        """mysql> create procedure p2(p_age int)
    -> begin
    -> select pname,ticnumber,sex from passenger where age>p_age;
    -> end//
Query OK, 0 rows affected (0.00 sec)

mysql> call p2(30)//

mysql> call p2(24)//""",
        """-- Result of call p2(30)//
+-------+-----------+------+
| pname | ticnumber | sex  |
+-------+-----------+------+
| subbu | 1111      | m    |
| nirma | 5555      | f    |
+-------+-----------+------+
2 rows in set (0.00 sec)

-- Result of call p2(24)//
+-------+-----------+------+
| pname | ticnumber | sex  |
+-------+-----------+------+
| subbu | 1111      | m    |
| padma | 3333      | f    |
| nirma | 5555      | f    |
+-------+-----------+------+
3 rows in set (0.00 sec)"""
    )

    c2 = make_sql_card("PROC-02", "2. Stored Procedure 'p3' (Journey Duration > 10 Hours)",
        """mysql> create procedure p3()
    -> begin
    -> select source,dest from ticket555 where hour(timediff(reatime,deptime))>10;
    -> end//
Query OK, 0 rows affected (0.02 sec)

mysql> call p3()//""",
        """+--------+------+
| source | dest |
+--------+------+
| hyd    | srpt |
| hyd    | vij  |
+--------+------+
2 rows in set (0.00 sec)"""
    )

    return f'''
    <section id="sec-week-11" class="lab-section" data-week="week-11">
        {header}
        {c1}
        {c2}
    </section>
    '''

def build_week12_html():
    sql_all = """-- WEEK 12 COMPLETE CURSORS SCRIPT
-- 1. Cursor Procedure mycur1 (Single Parameter Passenger Lookup)
create procedure mycur1(pa_id int)
begin
    declare v_id int;
    declare v_name varchar(30);
    declare c1 cursor for select pnrno,pname from passenger where pnrno=pa_id;
    open c1;
    fetch c1 into v_id,v_name;
    select v_id,v_name;
    close c1;
end//

-- Call mycur1
call mycur1(1001)//

-- 2. Cursor Procedure mycur5 (Ticket Route Lookup)
create procedure mycur5(ti_id int)
begin
    declare x_no int;
    declare x_src varchar(30);
    declare x_dst varchar(30);
    declare c2 cursor for select tic_no,source,dest from ticket555 where tic_no=ti_id;
    open c2;
    fetch c2 into x_no,x_src,x_dst;
    select x_no,x_src,x_dst;
    close c2;
end//

-- Call mycur5
call mycur5(1111)//"""

    header = make_week_header(
        "week-12", "12", "Week 12: Database Cursors", "CO3",
        "Implementation of database cursors inside stored procedures to process multi-row query result sets tuple-by-tuple: DECLARE cursor, OPEN, FETCH into local variables, and CLOSE.",
        sql_all
    )

    c1 = make_sql_card("CURS-01", "1. Cursor Procedure 'mycur1' (Passenger Lookup)",
        """mysql> create procedure mycur1(pa_id int)
    -> begin
    -> declare v_id int;
    -> declare v_name varchar(30);
    -> declare c1 cursor for select pnrno,pname from passenger where pnrno=pa_id;
    -> open c1;
    -> fetch c1 into v_id,v_name;
    -> select v_id,v_name;
    -> close c1;
    -> end//
Query OK, 0 rows affected (0.00 sec)

mysql> call mycur1(1001)//""",
        """+------+--------+
| v_id | v_name |
+------+--------+
| 1001 | subbu  |
+------+--------+
1 row in set (0.01 sec)""",
        "Lifecycle: 1) DECLARE c1 CURSOR FOR SELECT, 2) OPEN c1, 3) FETCH c1 INTO variables, 4) CLOSE c1."
    )

    c2 = make_sql_card("CURS-02", "2. Cursor Procedure 'mycur5' (Ticket Route Lookup)",
        """mysql> create procedure mycur5(ti_id int)
    -> begin
    -> declare x_no int;
    -> declare x_src varchar(30);
    -> declare x_dst varchar(30);
    -> declare c2 cursor for select tic_no,source,dest from ticket555 where tic_no=ti_id;
    -> open c2;
    -> fetch c2 into x_no,x_src,x_dst;
    -> select x_no,x_src,x_dst;
    -> close c2;
    -> end//
Query OK, 0 rows affected (0.00 sec)

mysql> call mycur5(1111)//""",
        """+------+-------+-------+
| x_no | x_src | x_dst |
+------+-------+-------+
| 1111 | srpt  | hyd   |
+------+-------+-------+
1 row in set (0.00 sec)"""
    )

    return f'''
    <section id="sec-week-12" class="lab-section" data-week="week-12">
        {header}
        {c1}
        {c2}
    </section>
    '''

def build_raw_doc_html(raw_manual_text):
    escaped_raw = html.escape(raw_manual_text)
    total_chars = len(raw_manual_text)
    total_lines = len(raw_manual_text.splitlines())
    words_count = len(raw_manual_text.split())

    return f'''
    <section id="sec-raw-doc" class="lab-section raw-section" data-week="raw-doc">
        <div class="raw-doc-header terminal-card">
            <div class="raw-title-row">
                <div class="raw-badge-group">
                    <span class="raw-pill">SECTION 13 // RAW FILE AT LAST</span>
                    <span class="status-pill pulse-green">VERBATIM COPY</span>
                    <span class="clipboard-pill" id="raw-badge-status">✔ AUTO-COPIED ON OPEN</span>
                </div>
                <div class="raw-actions">
                    <button class="btn-term btn-primary" id="btn-copy-raw-manual" onclick="copyFullRawDocument()">
                        <span class="btn-icon">📋</span> Copy Raw Document
                    </button>
                    <button class="btn-term" onclick="downloadRawManual()">
                        <span class="btn-icon">💾</span> Download .txt
                    </button>
                    <button class="btn-term" onclick="selectRawText()">
                        <span class="btn-icon">📄</span> Select All
                    </button>
                </div>
            </div>
            <h2 class="raw-heading">FULL RAW DOCUMENT COPY (EXACT VERBATIM)</h2>
            <p class="raw-meta">
                Source: <code>DBMS_LAB_MANUAL---2025-26 II-I SEM(updated).docx</code> &nbsp;|&nbsp; 
                Characters: <strong>{total_chars:,}</strong> &nbsp;|&nbsp; 
                Lines: <strong>{total_lines:,}</strong> &nbsp;|&nbsp; 
                Words: <strong>{words_count:,}</strong> &nbsp;|&nbsp; 
                Encoding: <strong>UTF-8</strong>
            </p>
            <div class="raw-auto-copy-banner">
                <span class="banner-icon">⚡</span>
                <span class="banner-text"><strong>AUTOMATIC CLIPBOARD INTEGRATION:</strong> This complete raw document was automatically copied to your clipboard the moment this page loaded! You can immediately paste it anywhere with <kbd>Ctrl</kbd>+<kbd>V</kbd> (<kbd>Cmd</kbd>+<kbd>V</kbd>). Click the copy button above anytime to re-copy.</span>
            </div>
        </div>

        <div class="terminal-raw-viewer terminal-card">
            <div class="raw-viewer-bar">
                <span class="viewer-dot dot-red"></span>
                <span class="viewer-dot dot-yellow"></span>
                <span class="viewer-dot dot-green"></span>
                <span class="viewer-title">raw_manual_verbatim.txt [READ-ONLY BUFFER]</span>
                <span class="viewer-status">100% VERBATIM</span>
            </div>
            <div class="raw-content-wrapper">
                <pre id="raw-verbatim-text" class="raw-code"><code>{escaped_raw}</code></pre>
            </div>
        </div>
    </section>
    '''

print("Weeks 8 to 12 and Raw Document ready.")

