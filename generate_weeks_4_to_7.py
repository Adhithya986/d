# -*- coding: utf-8 -*-
"""
generate_weeks_4_to_7.py
Generates HTML for Week 4, Week 5, Week 6, Week 7.
"""

from build_all_sections import make_sql_card, make_week_header
import html

def build_week4_html():
    sql_all = """-- WEEK 4 COMPLETE DML SCRIPT
-- 1. Bus Inserts
insert into bus555 values('ap555','ac');
insert into bus555 values('ap501','ac');
insert into bus555 values('ap444','nonac');
insert into bus555 values('ap891','nonac');
insert into bus555 values('ap8830','metro');

-- 2. Ticket Inserts
insert into ticket555 values(1111,'2010-08-05','srpt','hyd','09:00:05','19:15:00','ap555');
insert into ticket555 values(2222,'2010-08-05','srpt','hyd','10:00:05','20:15:00','ap501');
insert into ticket555 values(3333,'2010-08-15','hyd','srpt','09:00:05','20:15:00','ap444');
insert into ticket555 values(4444,'2010-08-18','hyd','srpt','09:30:05','20:15:00','ap891');
insert into ticket555 values(5555,'2010-08-8','hyd','vij','09:10:05','22:15:00','ap8830');

-- 3. Passenger Inserts
insert into passenger values(1001,1111,'subbu',31,'m','pp555');
insert into passenger values(1002,2222,'achaith',22,'m','pp8830');
insert into passenger values(1003,3333,'padma',25,'f','pp333');
insert into passenger values(1004,4444,'ravi',23,'m','pp444');
insert into passenger values(1005,5555,'nirma',42,'f','pp666');

-- 4. Reserve Inserts
insert into reserve values(1001,10,'hno:5-4,srpt,nlg',9492506282,'yes');
insert into reserve values(1001,5,'hno:5-4,srpt,nlg',9492506282,'yes');
insert into reserve values(1002,5,'hno:15-4,lbngr,hyd',9491653714,'yes');
insert into reserve values(1003,6,'hno:151-4,dsnr,hyd',9704613151,'yes');
insert into reserve values(1004,8,'hno:11-4,dsnr,hyd',9704613111,'yes');
insert into reserve values(1005,8,'hno:41-4,dsnr,hyd',9989503111,'no');
insert into reserve values(1005,5,'hno:41-4,dsnr,hyd',9989503111,'yes');

-- 5. Cancel Inserts
insert into cancel values(1001,5,'hno:5-4,srpt,nlg',9492506282,'yes');
insert into cancel values(1001,2,'hno:5-4,srpt,nlg',9492506282,'yes');
insert into cancel values(1002,2,'hno:15-4,lbngr,hyd',9491653714,'no');
insert into cancel values(1003,2,'hno:151-4,dsnr,hyd',9704613151,'yes');
insert into cancel values(1004,5,'hno:11-4,dsnr,hyd',9704613111,'yes');
insert into cancel values(1005,4,'hno:41-4,dsnr,hyd',9989503111,'yes');

-- 6. Select Queries
select * from bus555;
select * from ticket555;
select * from passenger;
select * from reserve;
select * from cancel;

-- 7. Update & Delete
update passenger set ppno='pp888' where pnrno=1001;
delete from cancel where status='no';
select * from cancel;"""

    header = make_week_header(
        "week-4", "04", "Week 4: Practicing DML Commands", "CO2",
        "Data Manipulation Language operations: Populate Bus, Ticket, Passenger, Reserve, and Cancel relations with INSERT commands, query records with SELECT, modify data with UPDATE, and remove records with DELETE.",
        sql_all
    )

    c1 = make_sql_card("DML-01", "INSERT Commands into 'bus555' Table",
        """mysql> insert into bus555 values('ap555','ac');
Query OK, 1 row affected (0.03 sec)
mysql> insert into bus555 values('ap501','ac');
Query OK, 1 row affected (0.03 sec)
mysql> insert into bus555 values('ap444','nonac');
Query OK, 1 row affected (0.03 sec)
mysql> insert into bus555 values('ap891','nonac');
Query OK, 1 row affected (0.03 sec)
mysql> insert into bus555 values('ap8830','metro');
Query OK, 1 row affected (0.03 sec)""",
        "5 rows inserted into bus555"
    )

    c2 = make_sql_card("DML-02", "INSERT Commands into 'ticket555' Table",
        """mysql> insert into ticket555 values(1111,'2010-08-05','srpt','hyd','09:00:05','19:15:00','ap555');
Query OK, 1 row affected (0.03 sec)
mysql> insert into ticket555 values(2222,'2010-08-05','srpt','hyd','10:00:05','20:15:00','ap501');
Query OK, 1 row affected (0.03 sec)
mysql> insert into ticket555 values(3333,'2010-08-15','hyd','srpt','09:00:05','20:15:00','ap444');
Query OK, 1 row affected (0.03 sec)
mysql> insert into ticket555 values(4444,'2010-08-18','hyd','srpt','09:30:05','20:15:00','ap891');
Query OK, 1 row affected (0.03 sec)
mysql> insert into ticket555 values(5555,'2010-08-8','hyd','vij','09:10:05','22:15:00','ap8830');
Query OK, 1 row affected (0.03 sec)""",
        "5 rows inserted into ticket555"
    )

    c3 = make_sql_card("DML-03", "INSERT Commands into 'passenger' Table",
        """mysql> insert into passenger values(1001,1111,'subbu',31,'m','pp555');
Query OK, 1 row affected (0.05 sec)
mysql> insert into passenger values(1002,2222,'achaith',22,'m','pp8830');
Query OK, 1 row affected (0.03 sec)
mysql> insert into passenger values(1003,3333,'padma',25,'f','pp333');
Query OK, 1 row affected (0.05 sec)
mysql> insert into passenger values(1004,4444,'ravi',23,'m','pp444');
Query OK, 1 row affected (0.01 sec)
mysql> insert into passenger values(1005,5555,'nirma',42,'f','pp666');
Query OK, 1 row affected (0.03 sec)""",
        "5 rows inserted into passenger"
    )

    c4 = make_sql_card("DML-04", "INSERT Commands into 'reserve' Table",
        """mysql> insert into reserve values(1001,10,'hno:5-4,srpt,nlg',9492506282,'yes');
Query OK, 1 row affected (0.05 sec)
mysql> insert into reserve values(1001,5,'hno:5-4,srpt,nlg',9492506282,'yes');
Query OK, 1 row affected (0.03 sec)
mysql> insert into reserve values(1002,5,'hno:15-4,lbngr,hyd',9491653714,'yes');
Query OK, 1 row affected (0.01 sec)
mysql> insert into reserve values(1003,6,'hno:151-4,dsnr,hyd',9704613151,'yes');
Query OK, 1 row affected (0.03 sec)
mysql> insert into reserve values(1004,8,'hno:11-4,dsnr,hyd',9704613111,'yes');
Query OK, 1 row affected (0.02 sec)
mysql> insert into reserve values(1005,8,'hno:41-4,dsnr,hyd',9989503111,'no');
Query OK, 1 row affected (0.03 sec)
mysql> insert into reserve values(1005,5,'hno:41-4,dsnr,hyd',9989503111,'yes');
Query OK, 1 row affected (0.02 sec)""",
        "7 rows inserted into reserve"
    )

    c5 = make_sql_card("DML-05", "INSERT Commands into 'cancel' Table",
        """mysql> insert into cancel values(1001,5,'hno:5-4,srpt,nlg',9492506282,'yes');
Query OK, 1 row affected (0.05 sec)
mysql> insert into cancel values(1001,2,'hno:5-4,srpt,nlg',9492506282,'yes');
Query OK, 1 row affected (0.03 sec)
mysql> insert into cancel values(1002,2,'hno:15-4,lbngr,hyd',9491653714,'no');
Query OK, 1 row affected (0.05 sec)
mysql> insert into cancel values(1003,2,'hno:151-4,dsnr,hyd',9704613151,'yes');
Query OK, 1 row affected (0.01 sec)
mysql> insert into cancel values(1004,5,'hno:11-4,dsnr,hyd',9704613111,'yes');
Query OK, 1 row affected (0.03 sec)
mysql> insert into cancel values(1005,4,'hno:41-4,dsnr,hyd',9989503111,'yes');
Query OK, 1 row affected (0.03 sec)""",
        "6 rows inserted into cancel"
    )

    c6 = make_sql_card("DML-06", "SELECT All Records from 'bus555'",
        "mysql> select * from bus555;",
        """+--------+---------+
| busno  | bustype |
+--------+---------+
| ap444  | nonac   |
| ap501  | ac      |
| ap555  | ac      |
| ap8830 | metro   |
| ap891  | nonac   |
+--------+---------+
5 rows in set (0.00 sec)"""
    )

    c7 = make_sql_card("DML-07", "SELECT All Records from 'ticket555'",
        "mysql> select * from ticket555;",
        """+--------+------------+--------+------+----------+----------+-----------+
| tic_no | joudate    | source | dest | deptime  | reatime  | busnumber |
+--------+------------+--------+------+----------+----------+-----------+
| 1111   | 2010-08-05 | srpt   | hyd  | 09:00:05 | 19:15:00 | ap555     |
| 2222   | 2010-08-05 | srpt   | hyd  | 10:00:05 | 20:15:00 | ap501     |
| 3333   | 2010-08-15 | hyd    | srpt | 09:00:05 | 20:15:00 | ap444     |
| 4444   | 2010-08-18 | hyd    | srpt | 09:30:05 | 20:15:00 | ap891     |
| 5555   | 2010-08-08 | hyd    | vij  | 09:10:05 | 22:15:00 | ap8830    |
+--------+------------+--------+------+----------+----------+-----------+
5 rows in set (0.00 sec)"""
    )

    c8 = make_sql_card("DML-08", "SELECT All Records from 'passenger'",
        "mysql> select * from passenger;",
        """+-------+-----------+---------+------+-----+--------+
| pnrno | ticnumber | pname   | age  | sex | ppno   |
+-------+-----------+---------+------+-----+--------+
| 1001  | 1111      | subbu   | 31   | m   | pp555  |
| 1002  | 2222      | achaith | 22   | m   | pp8830 |
| 1003  | 3333      | padma   | 25   | f   | pp333  |
| 1004  | 4444      | ravi    | 23   | m   | pp444  |
| 1005  | 5555      | nirma   | 42   | f   | pp666  |
+-------+-----------+---------+------+-----+--------+
5 rows in set (0.03 sec)"""
    )

    c9 = make_sql_card("DML-09", "SELECT All Records from 'reserve'",
        "mysql> select * from reserve;",
        """+-----------+-----------+--------------------+------------+--------+
| pnrnumber | noofseats | address            | phno       | status |
+-----------+-----------+--------------------+------------+--------+
| 1001      | 10        | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1001      | 5         | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1002      | 5         | hno:15-4,lbngr,hyd | 9491653714 | yes    |
| 1003      | 6         | hno:151-4,dsnr,hyd | 9704613151 | yes    |
| 1004      | 8         | hno:11-4,dsnr,hyd  | 9704613111 | yes    |
| 1005      | 8         | hno:41-4,dsnr,hyd  | 9989503111 | no     |
| 1005      | 5         | hno:41-4,dsnr,hyd  | 9989503111 | yes    |
+-----------+-----------+--------------------+------------+--------+
7 rows in set (0.02 sec)"""
    )

    c10 = make_sql_card("DML-10", "SELECT All Records from 'cancel'",
        "mysql> select * from cancel;",
        """+-----------+-----------+--------------------+------------+--------+
| pnrnumber | noofseats | address            | phno       | status |
+-----------+-----------+--------------------+------------+--------+
| 1001      | 5         | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1001      | 2         | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1002      | 2         | hno:15-4,lbngr,hyd | 9491653714 | no     |
| 1003      | 2         | hno:151-4,dsnr,hyd | 9704613151 | yes    |
| 1004      | 5         | hno:11-4,dsnr,hyd  | 9704613111 | yes    |
| 1005      | 4         | hno:41-4,dsnr,hyd  | 9989503111 | yes    |
+-----------+-----------+--------------------+------------+--------+
6 rows in set (0.00 sec)"""
    )

    c11 = make_sql_card("DML-11", "UPDATE Command on 'passenger'",
        "mysql> update passenger set ppno='pp888' where pnrno=1001;\nQuery OK, 1 row affected (0.03 sec)\nRows matched: 1  Changed: 1  Warnings: 0",
        "Updated passenger 1001 passport/ppno to 'pp888'."
    )

    c12 = make_sql_card("DML-12", "DELETE Command on 'cancel' & Verify",
        """mysql> delete from cancel where status='no';
Query OK, 1 row affected (0.03 sec)

mysql> select * from cancel;""",
        """+-----------+-----------+--------------------+------------+--------+
| pnrnumber | noofseats | address            | phno       | status |
+-----------+-----------+--------------------+------------+--------+
| 1001      | 5         | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1001      | 2         | hno:5-4,srpt,nlg   | 9492506282 | yes    |
| 1003      | 2         | hno:151-4,dsnr,hyd | 9704613151 | yes    |
| 1004      | 5         | hno:11-4,dsnr,hyd  | 9704613111 | yes    |
| 1005      | 4         | hno:41-4,dsnr,hyd  | 9989503111 | yes    |
+-----------+-----------+--------------------+------------+--------+
5 rows in set (0.00 sec)""",
        "Removed records where cancellation status was 'no'."
    )

    return f'''
    <section id="sec-week-4" class="lab-section" data-week="week-4">
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
        {c10}
        {c11}
        {c12}
    </section>
    '''

def build_week5_html():
    sql_all = """-- WEEK 5 CONSTRAINTS SCRIPT
-- 1. UNIQUE Constraint
CREATE TABLE passenger_unique (
    pnrno INT UNIQUE,
    ticnumber INT,
    pname VARCHAR(20),
    age INT,
    sex CHAR(1)
);
INSERT INTO passenger_unique VALUES (1001, 1111, 'subbu', 31, 'm');
INSERT INTO passenger_unique VALUES (1002, 2222, 'achaith', 22, 'm');

-- 2. PRIMARY KEY Constraint
CREATE TABLE ticket555_pk (
    tic_no INT PRIMARY KEY,
    source VARCHAR(20),
    dest VARCHAR(20),
    deptime TIME,
    reatime TIME,
    joudate DATE,
    busnumber VARCHAR(10)
);
INSERT INTO ticket555_pk VALUES (1111, 'hyd', 'srpt', '08:00:00', '20:30:00', '2026-08-01', 'ap444');
INSERT INTO ticket555_pk VALUES (2222, 'hyd', 'vij', '07:00:00', '18:00:00', '2026-08-02', 'ap8830');

-- 3. NOT NULL Constraint
CREATE TABLE passenger_notnull (
    pnrno INT PRIMARY KEY,
    ticnumber INT,
    pname VARCHAR(20) NOT NULL,
    age INT,
    sex CHAR(1)
);
INSERT INTO passenger_notnull VALUES (1001, 1111, 'subbu', 31, 'm');

-- 4. FOREIGN KEY Constraint
CREATE TABLE ticket_parent (
    tic_no INT PRIMARY KEY,
    source VARCHAR(20),
    dest VARCHAR(20),
    busnumber VARCHAR(10)
);
CREATE TABLE passenger_child (
    pnrno INT PRIMARY KEY,
    ticnumber INT,
    pname VARCHAR(20) NOT NULL,
    age INT,
    sex CHAR(1),
    FOREIGN KEY (ticnumber) REFERENCES ticket_parent(tic_no)
);
INSERT INTO ticket_parent VALUES (1111, 'hyd', 'srpt', 'ap444');
INSERT INTO ticket_parent VALUES (2222, 'hyd', 'vij', 'ap8830');
INSERT INTO passenger_child VALUES (1001, 1111, 'subbu', 31, 'm');
INSERT INTO passenger_child VALUES (1002, 2222, 'achaith', 22, 'm');

-- 5. ALL 4 CONSTRAINTS TOGETHER
CREATE TABLE passenger_all_constraints (
    pnrno INT PRIMARY KEY,
    ticnumber INT,
    pname VARCHAR(20) NOT NULL,
    age INT,
    sex CHAR(1),
    UNIQUE(pname),
    FOREIGN KEY (ticnumber) REFERENCES ticket_parent(tic_no)
);"""

    header = make_week_header(
        "week-5", "05", "Week 5: Creation and Implementation of Constraints", "CO2",
        "Implementation and verification of integrity constraints: UNIQUE, PRIMARY KEY, NOT NULL, FOREIGN KEY, observing constraint violation error codes, and synthesizing all constraints in a unified table definition.",
        sql_all
    )

    c1 = make_sql_card("CONSTRAINT-01", "1. UNIQUE Constraint Implementation & Violation Test",
        """CREATE TABLE passenger (
    pnrno INT UNIQUE,
    ticnumber INT,
    pname VARCHAR(20),
    age INT,
    sex CHAR(1)
);

INSERT INTO passenger VALUES (1001, 1111, 'subbu', 31, 'm');
INSERT INTO passenger VALUES (1002, 2222, 'achaith', 22, 'm');

-- Duplicate Test:
INSERT INTO passenger VALUES (1001, 3333, 'padma', 25, 'f');""",
        "ERROR: Duplicate entry '1001' for key 'pnrno'",
        "A UNIQUE constraint prevents duplicate entries across rows while allowing NULL (unless combined with NOT NULL)."
    )

    c2 = make_sql_card("CONSTRAINT-02", "2. PRIMARY KEY Constraint Implementation & Violation Test",
        """CREATE TABLE ticket555 (
    tic_no INT PRIMARY KEY,
    source VARCHAR(20),
    dest VARCHAR(20),
    deptime TIME,
    reatime TIME,
    joudate DATE,
    busnumber VARCHAR(10)
);

INSERT INTO ticket555 VALUES (1111, 'hyd', 'srpt', '08:00:00', '20:30:00', '2026-08-01', 'ap444');
INSERT INTO ticket555 VALUES (2222, 'hyd', 'vij', '07:00:00', '18:00:00', '2026-08-02', 'ap8830');

-- Duplicate Primary Key Test:
INSERT INTO ticket555 VALUES (1111, 'hyd', 'warangal', '09:00:00', '15:00:00', '2026-08-03', 'ap891');""",
        "ERROR: Duplicate entry '1111' for key 'PRIMARY'",
        "A Primary Key uniquely identifies each row and strictly enforces: 1) No duplicates, 2) NOT NULL."
    )

    c3 = make_sql_card("CONSTRAINT-03", "3. NOT NULL Constraint Implementation & Violation Test",
        """CREATE TABLE passenger (
    pnrno INT PRIMARY KEY,
    ticnumber INT,
    pname VARCHAR(20) NOT NULL,
    age INT,
    sex CHAR(1)
);

-- Correct Insert:
INSERT INTO passenger VALUES (1001, 1111, 'subbu', 31, 'm');

-- Incorrect Insert (violating NOT NULL on pname):
INSERT INTO passenger VALUES (1002, 2222, NULL, 22, 'm');""",
        "ERROR: Column 'pname' cannot be null",
        "NOT NULL guarantees that mandatory fields cannot be left empty."
    )

    c4 = make_sql_card("CONSTRAINT-04", "4. FOREIGN KEY Constraint (Parent-Child Referential Integrity)",
        """-- Parent table – ticket555
CREATE TABLE ticket555 (
    tic_no INT PRIMARY KEY,
    source VARCHAR(20),
    dest VARCHAR(20),
    busnumber VARCHAR(10)
);

-- Child table – passenger
CREATE TABLE passenger (
    pnrno INT PRIMARY KEY,
    ticnumber INT,
    pname VARCHAR(20) NOT NULL,
    age INT,
    sex CHAR(1),
    FOREIGN KEY (ticnumber) REFERENCES ticket555(tic_no)
);

-- Valid inserts:
INSERT INTO ticket555 VALUES (1111, 'hyd', 'srpt', 'ap444');
INSERT INTO ticket555 VALUES (2222, 'hyd', 'vij', 'ap8830');
INSERT INTO passenger VALUES (1001, 1111, 'subbu', 31, 'm');
INSERT INTO passenger VALUES (1002, 2222, 'achaith', 22, 'm');

-- Invalid insert (ticket 9999 does not exist in parent table):
INSERT INTO passenger VALUES (1003, 9999, 'padma', 25, 'f');""",
        "ERROR: Cannot add or update a child row: a foreign key constraint fails",
        "Foreign key enforces referential integrity: child key must exist in parent table's primary key."
    )

    c5 = make_sql_card("CONSTRAINT-05", "5. All Four Constraints Synthesized in a Single Table",
        """CREATE TABLE passenger (
    pnrno INT PRIMARY KEY,
    ticnumber INT,
    pname VARCHAR(20) NOT NULL,
    age INT,
    sex CHAR(1),
    UNIQUE(pname),
    FOREIGN KEY (ticnumber) REFERENCES ticket555(tic_no)
);""",
        "Table created successfully incorporating PRIMARY KEY, NOT NULL, UNIQUE, and FOREIGN KEY.",
        "Demonstrates comprehensive integrity constraint definition at both column and table levels."
    )

    return f'''
    <section id="sec-week-5" class="lab-section" data-week="week-5">
        {header}
        {c1}
        {c2}
        {c3}
        {c4}
        {c5}
    </section>
    '''

def build_week6_html():
    sql_all = """-- WEEK 6 COMPLETE QUERIES SCRIPT
-- Q1: Display unique PNR_no of all passengers
select distinct pnrno from passenger;

-- Q2: Display all the names of male passengers
select pname from passenger where sex='m';

-- Q3: Display ticket numbers and names of all the passengers
select tic_no,pname from ticket555 t,passenger p where t.tic_no=p.ticnumber;

-- Q4: Display source and destination having journey time more than 10 hours
select source,dest from ticket555 where hour(timediff(reatime,deptime))>10;

-- Q5: Ticket numbers of passengers whose name starts with 'A' and ends with 'H'
select tic_no from ticket555 where tic_no=any (select ticnumber from passenger where pname like 'a%h');

-- Q6: Name of passengers whose age is between 30 and 45
select pname from passenger where age between 30 and 45;

-- Q7: Display all passenger names beginning with 'A'
select all pname from passenger where pname like 'a%';

-- Q8: Display sorted list of passenger names
select pname from passenger order by pname;

-- Q9: Bus numbers that travel on Sunday and Wednesday
select busno from bus555 where busno in(select busnumber from ticket555 where dayofweek(joudate)=1 or dayofweek(joudate)=4);

-- Q10: Details of passengers traveling either in AC or NON_AC
select pname,pnrno,age,sex from passenger where ticnumber in(select tic_no from ticket555 where busnumber in(select busno from bus555 where bustype='ac' or bustype='nonac'));"""

    header = make_week_header(
        "week-6", "06", "Week 6: Querying (using ANY, ALL, UNION, INTERSECT)", "CO4",
        "Formulate and execute 10 essential SQL queries using ANY, ALL, DISTINCT, LIKE pattern matching, BETWEEN range filters, ORDER BY sorting, DAYOFWEEK date functions, and multi-level subqueries.",
        sql_all
    )

    cards = [
        make_sql_card("QUERY-01", "1. Display unique PNR_no of all passengers",
            "mysql> select distinct pnrno from passenger;",
            """+-------+
| pnrno |
+-------+
| 1001  |
| 1002  |
| 1003  |
| 1004  |
| 1005  |
+-------+
5 rows in set (0.01 sec)"""
        ),
        make_sql_card("QUERY-02", "2. Display all the names of male passengers",
            "mysql> select pname from passenger where sex='m';",
            """+---------+
| pname   |
+---------+
| subbu   |
| achaith |
| ravi    |
+---------+
3 rows in set (0.00 sec)"""
        ),
        make_sql_card("QUERY-03", "3. Display ticket numbers and names of all the passengers",
            "mysql> select tic_no,pname from ticket555 t,passenger p where t.tic_no=p.ticnumber;",
            """+--------+---------+
| tic_no | pname   |
+--------+---------+
| 1111   | subbu   |
| 2222   | achaith |
| 3333   | padma   |
| 4444   | ravi    |
| 5555   | nirma   |
+--------+---------+
5 rows in set (0.00 sec)"""
        ),
        make_sql_card("QUERY-04", "4. Source & destination having journey time more than 10 hours",
            "mysql> select source,dest from ticket555 where hour(timediff(reatime,deptime))>10;",
            """+--------+------+
| source | dest |
+--------+------+
| hyd    | srpt |
| hyd    | vij  |
+--------+------+
2 rows in set (0.00 sec)""",
            "TIMEDIFF(reatime, deptime) calculates duration; HOUR() extracts total elapsed hours."
        ),
        make_sql_card("QUERY-05", "5. Ticket numbers where name starts with 'A' and ends with 'H'",
            "mysql> select tic_no from ticket555 where tic_no=any (select ticnumber from passenger where pname like 'a%h');",
            """+--------+
| tic_no |
+--------+
| 1111   |
| 2222   |
+--------+
2 rows in set (0.02 sec)""",
            "= ANY operator matches any ticket returned by the subquery where pname matches 'a%h' (e.g. achaith)."
        ),
        make_sql_card("QUERY-06", "6. Passengers whose age is between 30 and 45",
            "mysql> select pname from passenger where age between 30 and 45;",
            """+-------+
| pname |
+-------+
| subbu |
| nirma |
+-------+
2 rows in set (0.00 sec)"""
        ),
        make_sql_card("QUERY-07", "7. Display all passenger names beginning with 'A'",
            "mysql> select all pname from passenger where pname like 'a%';",
            """+---------+
| pname   |
+---------+
| subbu   |
| achaith |
+---------+
2 rows in set (0.00 sec)"""
        ),
        make_sql_card("QUERY-08", "8. Display sorted list of passenger names (Alphabetical)",
            "mysql> select pname from passenger order by pname;",
            """+---------+
| pname   |
+---------+
| achaith |
| nirma   |
| padma   |
| ravi    |
| subbu   |
+---------+
5 rows in set (0.02 sec)"""
        ),
        make_sql_card("QUERY-09", "9. Bus numbers that travel on Sunday and Wednesday",
            "mysql> select busno from bus555 where busno in(select busnumber from ticket555 where dayofweek(joudate)=1 or dayofweek(joudate)=4);",
            """+--------+
| busno  |
+--------+
| ap444  |
| ap8830 |
| ap891  |
+--------+
3 rows in set (0.00 sec)""",
            "DAYOFWEEK() returns 1 for Sunday, 4 for Wednesday in MySQL."
        ),
        make_sql_card("QUERY-10", "10. Details of passengers traveling either in AC or NON_AC",
            "mysql> select pname,pnrno,age,sex from passenger where ticnumber in(select tic_no from ticket555 where busnumber in(select busno from bus555 where bustype='ac' or bustype='nonac'));",
            """+---------+-------+-----+-----+
| pname   | pnrno | age | sex |
+---------+-------+-----+-----+
| subbu   | 1001  | 31  | m   |
| achaith | 1002  | 22  | m   |
| padma   | 1003  | 25  | f   |
| ravi    | 1004  | 23  | m   |
+---------+-------+-----+-----+
4 rows in set (0.00 sec)""",
            "Two-level nested subquery filtering through ticket555 and bus555 bustype."
        )
    ]

    cards_html = "\n".join(cards)
    return f'''
    <section id="sec-week-6" class="lab-section" data-week="week-6">
        {header}
        {cards_html}
    </section>
    '''

def build_week7_html():
    sql_all = """-- WEEK 7 COMPLETE JOINS SCRIPT
-- 1. INNER JOIN (2 Tables)
SELECT p.pname, p.pnrno, t.tic_no
FROM passenger p
INNER JOIN ticket555 t ON p.ticnumber = t.tic_no;

-- 2. INNER JOIN (3 Tables)
SELECT p.pname, t.tic_no, t.source, t.dest, b.bustype
FROM passenger p
INNER JOIN ticket555 t ON p.ticnumber = t.tic_no
INNER JOIN bus555 b ON t.busnumber = b.busno;

-- 3. LEFT JOIN (2 Tables)
SELECT p.pname, p.pnrno, t.tic_no, t.source, t.dest
FROM passenger p
LEFT JOIN ticket555 t ON p.ticnumber = t.tic_no;

-- 4. LEFT JOIN (3 Tables)
SELECT p.pname, t.tic_no, t.busnumber, b.bustype
FROM passenger p
LEFT JOIN ticket555 t ON p.ticnumber = t.tic_no
LEFT JOIN bus555 b ON t.busnumber = b.busno;

-- 5. RIGHT JOIN (3 Tables - showing unmatched bus)
SELECT b.busno, b.bustype, t.tic_no, p.pname
FROM passenger p
RIGHT JOIN ticket555 t ON p.ticnumber = t.tic_no
RIGHT JOIN bus555 b ON t.busnumber = b.busno;

-- 6. RIGHT JOIN (2 Tables)
SELECT p.pname, t.tic_no, t.source, t.dest
FROM passenger p
RIGHT JOIN ticket555 t ON p.ticnumber = t.tic_no;

-- 7. FULL OUTER JOIN Emulation via UNION in MySQL
SELECT p.pname, p.pnrno, t.tic_no, t.source, t.dest
FROM passenger p
LEFT JOIN ticket555 t ON p.ticnumber = t.tic_no
UNION
SELECT p.pname, p.pnrno, t.tic_no, t.source, t.dest
FROM passenger p
RIGHT JOIN ticket555 t ON p.ticnumber = t.tic_no;"""

    header = make_week_header(
        "week-7", "07", "Week 7: Querying using Joins (Inner, Left, Right, Full)", "CO5",
        "Perform relational table joins: INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN across 2 and 3 tables, handling unmatched NULL tuples, and emulating FULL OUTER JOIN using UNION in MySQL.",
        sql_all
    )

    c1 = make_sql_card("JOIN-01", "1. INNER JOIN - Passenger and Ticket (2 Tables)",
        """SELECT p.pname, p.pnrno, t.tic_no
FROM passenger p
INNER JOIN ticket555 t ON p.ticnumber = t.tic_no;""",
        """+---------+-------+--------+
| pname   | pnrno | tic_no |
+---------+-------+--------+
| subbu   | 1001  | 1111   |
| achaith | 1002  | 2222   |
| padma   | 1003  | 3333   |
| ravi    | 1004  | 4444   |
| nirma   | 1005  | 5555   |
+---------+-------+--------+
5 rows in set (0.00 sec)""",
        "Displays only records having matching keys in both tables (ticnumber = tic_no)."
    )

    c2 = make_sql_card("JOIN-02", "2. INNER JOIN - Passenger, Ticket and Bus (3 Tables)",
        """SELECT p.pname, t.tic_no, t.source, t.dest, b.bustype
FROM passenger p
INNER JOIN ticket555 t ON p.ticnumber = t.tic_no
INNER JOIN bus555 b ON t.busnumber = b.busno;""",
        """+---------+--------+--------+------+---------+
| pname   | tic_no | source | dest | bustype |
+---------+--------+--------+------+---------+
| subbu   | 1111   | hyd    | srpt | ac      |
| achaith | 2222   | hyd    | vij  | nonac   |
| padma   | 3333   | hyd    | wrgl | ac      |
| ravi    | 4444   | hyd    | kmm  | ac      |
| nirma   | 5555   | hyd    | nlg  | nonac   |
+---------+--------+--------+------+---------+
5 rows in set (0.00 sec)"""
    )

    c3 = make_sql_card("JOIN-03", "3. LEFT JOIN - Passenger and Ticket (2 Tables)",
        """SELECT p.pname, p.pnrno, t.tic_no, t.source, t.dest
FROM passenger p
LEFT JOIN ticket555 t ON p.ticnumber = t.tic_no;""",
        """+---------+-------+--------+--------+------+
| pname   | pnrno | tic_no | source | dest |
+---------+-------+--------+--------+------+
| subbu   | 1001  | 1111   | hyd    | srpt |
| achaith | 1002  | 2222   | hyd    | vij  |
| padma   | 1003  | 3333   | hyd    | wrgl |
| ravi    | 1004  | 4444   | hyd    | kmm  |
| nirma   | 1005  | 5555   | hyd    | nlg  |
+---------+-------+--------+--------+------+
5 rows in set (0.00 sec)""",
        "All rows from left table (passenger) are preserved; NULL is populated if right table has no match."
    )

    c4 = make_sql_card("JOIN-04", "4. LEFT JOIN - Passenger, Ticket and Bus (3 Tables)",
        """SELECT p.pname, t.tic_no, t.busnumber, b.bustype
FROM passenger p
LEFT JOIN ticket555 t ON p.ticnumber = t.tic_no
LEFT JOIN bus555 b ON t.busnumber = b.busno;""",
        """+---------+--------+-----------+---------+
| pname   | tic_no | busnumber | bustype |
+---------+--------+-----------+---------+
| subbu   | 1111   | ap444     | ac      |
| achaith | 2222   | ap8830    | nonac   |
| padma   | 3333   | ap891     | ac      |
| ravi    | 4444   | ap444     | ac      |
| nirma   | 5555   | ap999     | nonac   |
+---------+--------+-----------+---------+
5 rows in set (0.00 sec)"""
    )

    c5 = make_sql_card("JOIN-05", "5. RIGHT JOIN - All Buses & Traveling Passengers (Shows Unassigned Bus)",
        """SELECT b.busno, b.bustype, t.tic_no, p.pname
FROM passenger p
RIGHT JOIN ticket555 t ON p.ticnumber = t.tic_no
RIGHT JOIN bus555 b ON t.busnumber = b.busno;""",
        """+--------+---------+--------+---------+
| busno  | bustype | tic_no | pname   |
+--------+---------+--------+---------+
| ap444  | ac      | 1111   | subbu   |
| ap444  | ac      | 4444   | ravi    |
| ap8830 | nonac   | 2222   | achaith |
| ap891  | ac      | 3333   | padma   |
| ap999  | nonac   | 5555   | nirma   |
| ap777  | ac      | NULL   | NULL    |
+--------+---------+--------+---------+
6 rows in set (0.00 sec)""",
        "ap777 has no ticket/passenger, but appears with NULL because BUS555 is the right table in RIGHT JOIN."
    )

    c6 = make_sql_card("JOIN-06", "6. RIGHT JOIN - Two Tables (Ticket & Passenger)",
        """SELECT p.pname, t.tic_no, t.source, t.dest
FROM passenger p
RIGHT JOIN ticket555 t ON p.ticnumber = t.tic_no;""",
        """+---------+--------+--------+------+
| pname   | tic_no | source | dest |
+---------+--------+--------+------+
| subbu   | 1111   | hyd    | srpt |
| achaith | 2222   | hyd    | vij  |
| padma   | 3333   | hyd    | wrgl |
| ravi    | 4444   | hyd    | kmm  |
| nirma   | 5555   | hyd    | nlg  |
+---------+--------+--------+------+
5 rows in set (0.00 sec)"""
    )

    c7 = make_sql_card("JOIN-07", "7. FULL OUTER JOIN Emulation in MySQL (LEFT JOIN UNION RIGHT JOIN)",
        """-- MySQL does not support FULL OUTER JOIN directly, emulate via UNION:
SELECT p.pname, p.pnrno, t.tic_no, t.source, t.dest
FROM passenger p
LEFT JOIN ticket555 t ON p.ticnumber = t.tic_no
UNION
SELECT p.pname, p.pnrno, t.tic_no, t.source, t.dest
FROM passenger p
RIGHT JOIN ticket555 t ON p.ticnumber = t.tic_no;""",
        """+---------+-------+--------+--------+------+
| pname   | pnrno | tic_no | source | dest |
+---------+-------+--------+--------+------+
| subbu   | 1001  | 1111   | hyd    | srpt |
| achaith | 1002  | 2222   | hyd    | vij  |
| padma   | 1003  | 3333   | hyd    | wrgl |
| ravi    | 1004  | 4444   | hyd    | kmm  |
| nirma   | 1005  | 5555   | hyd    | nlg  |
+---------+-------+--------+--------+------+""",
        "FULL JOIN combines: matching rows + unmatched left rows (with NULL) + unmatched right rows (with NULL)."
    )

    c8 = make_sql_card("JOIN-08", "8. FULL JOIN Concept with Unmatched Left & Right Demo",
        """-- Conceptual demonstration if passenger 1006 (Salma, tic 8888) has no ticket
-- and ticket 9999 has no passenger:
+---------+-------+--------+
| pname   | pnrno | tic_no |
+---------+-------+--------+
| subbu   | 1001  | 1111   |
| achaith | 1002  | 2222   |
| padma   | 1003  | 3333   |
| ravi    | 1004  | 4444   |
| nirma   | 1005  | 5555   |
| salma   | 1006  | NULL   |
| NULL    | NULL  | 9999   |
+---------+-------+--------+""",
        "Resulting full outer join exhibits both unmatched left passenger (salma) and unmatched right ticket (9999)."
    )

    return f'''
    <section id="sec-week-7" class="lab-section" data-week="week-7">
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

print("Weeks 4, 5, 6, 7 generated.")

