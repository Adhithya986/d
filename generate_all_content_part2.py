# -*- coding: utf-8 -*-
"""
Continuation of generate_all_content.py: Week 2, Week 3, Week 4, Week 5
"""

from build_all_sections import make_sql_card, make_week_header
import html

def build_week2_html():
    header = make_week_header(
        "week-2", "02", "Week 2: Database Normalization (1NF, 2NF, 3NF)", "CO1",
        "Design relational database tables to minimize duplication of information, eliminate insertion/update/deletion anomalies, and decompose Passenger, Bus, and Ticket relations through 1NF, 2NF, and 3NF."
    )
    return f'''
    <section id="sec-week-2" class="lab-section" data-week="week-2">
        {header}

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">THEORY</span>
                <span class="card-title">NORMALIZATION PRINCIPLES & NORMAL FORMS</span>
            </div>
            <p class="term-text">Database normalization is a technique for designing relational database tables to minimize duplication of information and, in doing so, safeguard the database against certain types of logical or structural problems namely <strong>data anomalies</strong> (Insertion, Deletion, and Update anomalies).</p>
            
            <div class="term-def-grid">
                <div class="def-box">
                    <span class="def-term">First Normal Form (1NF)</span>
                    <span class="def-desc">Requires that the values in each column of a table are <strong>atomic</strong>. No sets or repeating groups of values within a single column.</span>
                </div>
                <div class="def-box">
                    <span class="def-term">Second Normal Form (2NF)</span>
                    <span class="def-desc">Table must be in 1NF and all non-key columns must depend on the <strong>entire primary key</strong> (no partial functional dependencies on composite keys).</span>
                </div>
                <div class="def-box">
                    <span class="def-term">Third Normal Form (3NF)</span>
                    <span class="def-desc">Table must be in 2NF and all columns must depend directly on the primary key (no <strong>transitive dependencies</strong>: X → Y → Z).</span>
                </div>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">NORMALIZATION 01</span>
                <span class="card-title">NORMALIZATION OF PASSENGER ENTITY</span>
            </div>
            <p class="term-text">In the un-normalized passenger entity, passenger <strong>1001 (Subbu)</strong> contains two phone numbers in a single column (multivalued attribute violating 1NF):</p>
            
            <h4 class="term-subtitle">Un-normalized Passenger Table (Violates 1NF):</h4>
            <pre class="ascii-output"><code>+-------+---------+-----+-----+----------+----------+------------------------+---------+
| Pnrno | pname   | age | sex | ticketno | address  | phno                   | Catno   |
+-------+---------+-----+-----+----------+----------+------------------------+---------+
| 1001  | Subbu   | 31  | M   | 1111     | 5-4,srpt | 9492506282, 9848845985 | Cap5112 |
| 1002  | Achaith | 22  | M   | 2222     | 6-8,hyd  | 9949060540             | Cap6900 |
| 1003  | Padma   | 25  | F   | 3333     | h/7,vij  | 9704054050             | Cap5772 |
| 1004  | Ravi    | 23  | M   | 4444     | 8-9,hyd  | 9704613151             | Cap6132 |
| 1005  | Satyam  | 42  | F   | 5555     | 9-11,hyd | 9848354941             | Cap6732 |
+-------+---------+-----+-----+----------+----------+------------------------+---------+</code></pre>

            <h4 class="term-subtitle">Normalized Passenger Table (in 1NF, 2NF, and 3NF):</h4>
            <p class="term-text">Split multivalued values into atomic rows. As Pnrno is a single attribute primary key, no partial dependencies exist (2NF satisfied). No non-prime attribute determines another non-prime attribute (3NF satisfied):</p>
            <pre class="ascii-output"><code>+-------+---------+-----+-----+----------+----------+------------+---------+
| Pnrno | pname   | age | sex | ticketno | address  | phno       | Catno   |
+-------+---------+-----+-----+----------+----------+------------+---------+
| 1001  | Subbu   | 31  | M   | 1111     | 5-4,srpt | 9492506282 | Cap5112 |
| 1001  | Subbu   | 31  | M   | 1111     | 5-4,srpt | 9848845985 | Cap5112 |
| 1002  | Achaith | 22  | M   | 2222     | 6-8,hyd  | 9949060540 | Cap6900 |
| 1003  | Padma   | 25  | F   | 3333     | h/7,vij  | 9704054050 | Cap5772 |
| 1004  | Ravi    | 23  | M   | 4444     | 8-9,hyd  | 9704613151 | Cap6132 |
| 1005  | Satyam  | 42  | F   | 5555     | 9-11,hyd | 9848354941 | Cap6732 |
+-------+---------+-----+-----+----------+----------+------------+---------+</code></pre>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">NORMALIZATION 02</span>
                <span class="card-title">NORMALIZATION OF BUS ENTITY (ELIMINATING PARTIAL DEPENDENCIES)</span>
            </div>
            <p class="term-text">In the Bus entity, the composite primary key is <code>(Busno + serviceno)</code>. The following partial dependencies exist (violating 2NF):</p>
            <ul class="terminal-list">
                <li><code>Busno ----&gt; Bustype, Noofseats</code> (depends only on part of composite key)</li>
                <li><code>Serviceno ----&gt; Source, Dest</code> (depends only on part of composite key)</li>
            </ul>

            <h4 class="term-subtitle">Decomposition into 2NF &amp; 3NF Relations:</h4>
            <div class="grid-3-col">
                <div class="sub-card">
                    <span class="step-badge">TABLE 1</span>
                    <h5 class="term-subtitle">Bus_Schedule</h5>
                    <pre class="ascii-output"><code>+--------+-----------+----------+----------+
| Busno  | serviceno | deptime  | retime   |
+--------+-----------+----------+----------+
| Ap555  | 3889      | 9:00:00  | 19:15:00 |
| Ap501  | 3891      | 10:00:15 | 20:15:00 |
| Ap444  | 3601      | 9:00:00  | 19:30:00 |
| Ap891  | 3555      | 9:30:00  | 20:30:00 |
| Ap8830 | 3239      | 9:00:00  | 22:30:00 |
+--------+-----------+----------+----------+</code></pre>
                </div>
                <div class="sub-card">
                    <span class="step-badge">TABLE 2</span>
                    <h5 class="term-subtitle">Bus_Details</h5>
                    <pre class="ascii-output"><code>+--------+---------+-----------+
| Busno  | bustype | Noofseats |
+--------+---------+-----------+
| Ap555  | Ac      | 36        |
| Ap501  | Ac      | 36        |
| Ap444  | Nonac   | 52        |
| Ap891  | Nonac   | 52        |
| Ap8830 | Metro   | 45        |
+--------+---------+-----------+</code></pre>
                </div>
                <div class="sub-card">
                    <span class="step-badge">TABLE 3</span>
                    <h5 class="term-subtitle">Service_Route</h5>
                    <pre class="ascii-output"><code>+-----------+--------+-------------+
| serviceno | source | destination |
+-----------+--------+-------------+
| 3889      | Srpt   | Hyd         |
| 3891      | Srpt   | Hyd         |
| 3601      | Hyd    | Srpt        |
| 3555      | Hyd    | Srpt        |
| 3239      | Hyd    | Vij         |
+-----------+--------+-------------+</code></pre>
                </div>
            </div>
            <p class="term-text">All columns now depend directly on full primary keys without partial or transitive dependencies (Both 2NF and 3NF achieved).</p>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">NORMALIZATION 03</span>
                <span class="card-title">NORMALIZATION OF TICKET ENTITY (ELIMINATING TRANSITIVE DEPENDENCY)</span>
            </div>
            <p class="term-text">In Ticket entity, <code>Ticketno → Catcard</code> and <code>Catcard → Amount</code>. This transitive dependency (<code>Ticketno → Amount</code> via <code>Catcard</code>) violates 3NF.</p>
            <p class="term-text">Solution: Separate the category card discount and fare amount into an independent lookup relation.</p>

            <div class="grid-2-col">
                <div class="sub-card">
                    <span class="step-badge">RELATION 1</span>
                    <h5 class="term-subtitle">Ticket (in 3NF)</h5>
                    <pre class="ascii-output"><code>+----------+-----------+----------+--------+-------------+--------+---------+
| Ticketno | Joudate   | Joutime  | Source | Destination | Seatno | Catcard |
+----------+-----------+----------+--------+-------------+--------+---------+
| 1111     | 2010-8-5  | 9:00:00  | Srpt   | Hyd         | 5      | No      |
| 2222     | 2010-8-5  | 10:00:15 | Srpt   | Hyd         | 10     | Yes     |
| 3333     | 2010-8-15 | 9:00:00  | Hyd    | Srpt        | 15     | Yes     |
| 4444     | 2010-8-18 | 9:30:00  | Hyd    | Srpt        | 20     | No      |
| 5555     | 2010-8-6  | 9:00:00  | Hyd    | Vij         | 18     | Yes     |
+----------+-----------+----------+--------+-------------+--------+---------+</code></pre>
                </div>
                <div class="sub-card">
                    <span class="step-badge">RELATION 2</span>
                    <h5 class="term-subtitle">Category_Tariff (in 3NF)</h5>
                    <pre class="ascii-output"><code>+---------+--------+
| Catcard | Amount |
+---------+--------+
| No      | 96     |
| Yes     | 88     |
| Yes     | 172    |
+---------+--------+</code></pre>
                </div>
            </div>
            <p class="term-text"><strong>Result:</strong> All relations are normalized into 3NF and completely free from data redundancy, partial functional dependencies, and transitive dependencies.</p>
        </div>
    </section>
    '''

def build_week3_html():
    sql_all = """-- WEEK 3 COMPLETE SQL SCRIPT
show databases;
create database groupa;
use groupa;
create table groupamem(rollno numeric(10), name varchar(15), phone numeric(10), branch varchar(10));
desc groupamem;
alter table groupamem add gender char(3);
desc groupamem;
create table dd(name varchar(10));
show tables;
drop table dd;
create database dbl;
show databases;
drop database dbl;
show databases;
rename table groupamem to ga;
show tables;
insert into ga values(1111, 'ram', 9885321456, 'mbbs', 'm');
select * from ga;
truncate table ga;
select * from ga;

-- ROADWAY TRAVELS SYSTEM TABLES
create table bus555(busno varchar(10), bustype varchar(10), primary key(busno));
create table ticket555(tic_no numeric(10), joudate date, source varchar(10), dest varchar(10), deptime time, reatime time, busnumber varchar(10), primary key(tic_no));
alter table ticket555 add constraint tic_fk foreign key(busnumber) references bus555(busno);
create table passenger(pnrno numeric(10), ticnumber numeric(10), pname varchar(15), age int(4), sex char(10), ppno varchar(15), primary key(pnrno));
alter table passenger add constraint pas_fk foreign key(ticnumber) references ticket555(tic_no);
create table reserve(pnrnumber numeric(10), noofseats int(8), address varchar(50), phno numeric(10), status char(3));
alter table reserve add constraint res_fk foreign key(pnrnumber) references passenger(pnrno);
create table cancel(pnrnumber numeric(10), noofseats int(8), address varchar(50), phno numeric(10), status char(3));
alter table cancel add constraint can_fk foreign key(pnrnumber) references passenger(pnrno);"""

    header = make_week_header(
        "week-3", "03", "Week 3: MySQL Setup & Practicing DDL Commands", "CO3",
        "Installation of MySQL 5.0, creating databases, creating tables, altering schema, dropping tables/databases, rename, truncate, and creating Roadway Travels tables with integrity constraints.",
        sql_all
    )

    c1 = make_sql_card("DDL-01", "Show Databases & Create Database 'groupa'", 
        "mysql> show databases;\n\nmysql> create database groupa;\nQuery OK, 1 row affected (0.01 sec)\n\nmysql> use groupa;\nDatabase changed",
        "+--------------------+\n| Database           |\n+--------------------+\n| information_schema |\n| mysql              |\n| test               |\n+--------------------+\n3 rows in set (0.09 sec)"
    )

    c2 = make_sql_card("DDL-02", "Create Table 'groupamem' & Describe Structure",
        "mysql> create table groupamem(rollno numeric(10),name varchar(15),phone numeric(10),branch varchar(10));\nQuery OK, 0 rows affected (0.42 sec)\n\nmysql> desc groupamem;",
        "+--------+---------------+------+-----+---------+-------+\n| Field  | Type          | Null | Key | Default | Extra |\n+--------+---------------+------+-----+---------+-------+\n| rollno | decimal(10,0) | YES  |     | NULL    |       |\n| name   | varchar(15)   | YES  |     | NULL    |       |\n| phone  | decimal(10,0) | YES  |     | NULL    |       |\n| branch | varchar(10)   | YES  |     | NULL    |       |\n+--------+---------------+------+-----+---------+-------+\n4 rows in set (0.03 sec)"
    )

    c3 = make_sql_card("DDL-03", "Alter Table - Add Column 'gender'",
        "mysql> alter table groupamem add gender char(3);\nQuery OK, 0 rows affected (0.36 sec)\nRecords: 0  Duplicates: 0  Warnings: 0\n\nmysql> desc groupamem;",
        "+--------+---------------+------+-----+---------+-------+\n| Field  | Type          | Null | Key | Default | Extra |\n+--------+---------------+------+-----+---------+-------+\n| rollno | decimal(10,0) | YES  |     | NULL    |       |\n| name   | varchar(15)   | YES  |     | NULL    |       |\n| phone  | decimal(10,0) | YES  |     | NULL    |       |\n| branch | varchar(10)   | YES  |     | NULL    |       |\n| gender | char(3)       | YES  |     | NULL    |       |\n+--------+---------------+------+-----+---------+-------+\n5 rows in set (0.00 sec)"
    )

    c4 = make_sql_card("DDL-04", "Create & Drop Table 'dd'",
        "mysql> create table dd(name varchar(10));\nQuery OK, 0 rows affected (0.09 sec)\n\nmysql> show tables;\n\nmysql> drop table dd;\nQuery OK, 0 rows affected (0.06 sec)",
        "+------------------+\n| Tables_in_groupa |\n+------------------+\n| dd               |\n| groupamem        |\n+------------------+\n2 rows in set (0.00 sec)"
    )

    c5 = make_sql_card("DDL-05", "Create & Drop Database 'dbl'",
        "mysql> create database dbl;\nQuery OK, 1 row affected (0.01 sec)\n\nmysql> show databases;\n\nmysql> drop database dbl;\nQuery OK, 0 rows affected (0.00 sec)\n\nmysql> show databases;",
        "+--------------------+\n| Database           |\n+--------------------+\n| information_schema |\n| dbl                |\n| groupa             |\n| mysql              |\n| test               |\n+--------------------+\n5 rows in set (0.01 sec)"
    )

    c6 = make_sql_card("DDL-06", "Rename Table 'groupamem' to 'ga'",
        "mysql> rename table groupamem to ga;\nQuery OK, 0 rows affected (0.03 sec)\n\nmysql> show tables;",
        "+------------------+\n| Tables_in_groupa |\n+------------------+\n| ga               |\n+------------------+\n1 row in set (0.00 sec)"
    )

    c7 = make_sql_card("DDL-07", "Truncate Table 'ga'",
        "mysql> insert into ga values(1111,'ram',9885321456,'mbbs','m');\nQuery OK, 1 row affected (0.06 sec)\n\nmysql> select * from ga;\n\nmysql> truncate table ga;\nQuery OK, 1 row affected (0.09 sec)\n\nmysql> select * from ga;\nEmpty set (0.00 sec)",
        "+--------+------+------------+--------+--------+\n| rollno | name | phone      | branch | gender |\n+--------+------+------------+--------+--------+\n| 1111   | ram  | 9885321456 | mbbs   | m      |\n+--------+------+------------+--------+--------+\n1 row in set (0.01 sec)\n\nEmpty set (0.00 sec)",
        "TRUNCATE deletes all data rows and deallocates storage spaces, keeping table definition intact."
    )

    c8 = make_sql_card("DDL-08", "Roadway Travels System - Create Tables with Foreign Keys",
        """mysql> create table bus555(busno varchar(10),bustype varchar(10),primary key(busno));
Query OK, 0 rows affected (0.17 sec)

mysql> create table ticket555(tic_no numeric(10),joudate date,source varchar(10),dest varchar(10),deptime time,reatime time,busnumber varchar(10),primary key(tic_no));
Query OK, 0 rows affected (0.08 sec)

mysql> alter table ticket555 add constraint tic_fk foreign key(busnumber) references bus555(busno);
Query OK, 0 rows affected (0.16 sec)

mysql> create table passenger(pnrno numeric(10),ticnumber numeric(10),pname varchar(15),age int(4),sex char(10),ppno varchar(15),primary key(pnrno));
Query OK, 0 rows affected (0.06 sec)

mysql> alter table passenger add constraint pas_fk foreign key(ticnumber) references ticket555(tic_no);
Query OK, 0 rows affected (0.14 sec)

mysql> create table reserve(pnrnumber numeric(10),noofseats int(8),address varchar(50),phno numeric(10),status char(3));
Query OK, 0 rows affected (0.16 sec)

mysql> alter table reserve add constraint res_fk foreign key(pnrnumber) references passenger(pnrno);
Query OK, 0 rows affected (0.17 sec)

mysql> create table cancel(pnrnumber numeric(10),noofseats int(8),address varchar(50),phno numeric(10),status char(3));
Query OK, 0 rows affected (0.06 sec)

mysql> alter table cancel add constraint can_fk foreign key(pnrnumber) references passenger(pnrno);
Query OK, 0 rows affected (0.14 sec)""",
        "Tables Created: bus555, ticket555, passenger, reserve, cancel with primary keys and foreign key constraints.",
        "Foreign key constraints enforce referential integrity between parent and child relations."
    )

    return f'''
    <section id="sec-week-3" class="lab-section" data-week="week-3">
        {header}

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">INSTALLATION GUIDE</span>
                <span class="card-title">MYSQL 5.0 SERVER SETUP WIZARD & CONFIGURATION (STEPS 1 - 19)</span>
            </div>
            <div class="installer-grid">
                <div class="install-step-box">
                    <span class="step-badge">STEPS 2 & 3</span>
                    <p class="term-text">Setup Type: Select Typical Installation</p>
                    <img src="images/image22.jpeg" alt="MySQL Installation Steps 2 & 3" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 4 & 5</span>
                    <p class="term-text">Ready to Install & Copying Program Files</p>
                    <img src="images/image23.jpeg" alt="MySQL Installation Steps 4 & 5" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 6 & 7</span>
                    <p class="term-text">MySQL Enterprise & Configuration Wizard launch</p>
                    <img src="images/image24.jpeg" alt="MySQL Installation Steps 6 & 7" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 8 & 9</span>
                    <p class="term-text">Instance Config: Select Detailed Configuration</p>
                    <img src="images/image25.jpeg" alt="MySQL Installation Steps 8 & 9" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 10 & 11</span>
                    <p class="term-text">Server Type: Developer Machine, Multifunctional DB</p>
                    <img src="images/image26.jpeg" alt="MySQL Installation Steps 10 & 11" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 12 & 13</span>
                    <p class="term-text">InnoDB Tablespace & Concurrent Connections (DSS/OLAP)</p>
                    <img src="images/image27.jpeg" alt="MySQL Installation Steps 12 & 13" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 14 & 15</span>
                    <p class="term-text">Networking (Port 3306) & Standard Character Set</p>
                    <img src="images/image28.jpeg" alt="MySQL Installation Steps 14 & 15" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 16 & 17</span>
                    <p class="term-text">Windows Service Name (MySQL) & Root Security Password</p>
                    <img src="images/image29.jpeg" alt="MySQL Installation Steps 16 & 17" class="term-img">
                </div>
                <div class="install-step-box">
                    <span class="step-badge">STEPS 18 & 19</span>
                    <p class="term-text">Execute Configuration & MySQL Command Line Client</p>
                    <img src="images/image30.jpeg" alt="MySQL Installation Steps 18 & 19" class="term-img">
                </div>
            </div>
        </div>

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

print("Weeks 2 & 3 generated.")

