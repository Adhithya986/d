# -*- coding: utf-8 -*-
"""
Build script for VBIT DBMS Lab Manual Terminal Web Page
"""

import os
import re
import json

with open('raw_manual.txt', 'r', encoding='utf-8') as f:
    raw_manual_text = f.read()

# Partition raw text into sections
section_pattern = re.compile(r'^(Week[\s:-]+\d+.*|DEPARTMENT OF COMPUTER SCIENCE.*)', re.MULTILINE | re.IGNORECASE)
splits = list(section_pattern.finditer(raw_manual_text))

raw_sections = []
for i in range(len(splits)):
    start = splits[i].start()
    end = splits[i+1].start() if i+1 < len(splits) else len(raw_manual_text)
    hdr = splits[i].group(0).strip()
    sec_content = raw_manual_text[start:end]
    raw_sections.append((hdr, sec_content))

print(f"Loaded {len(raw_sections)} sections from raw manual.")

# Define metadata for each section
sections_meta = [
    {
        "id": "sec-overview",
        "num": "00",
        "badge": "INFO",
        "title": "Overview & Lab Guidelines",
        "short_title": "Overview",
        "co": "CO1 - CO5",
        "desc": "VBIT Guidelines, Vision/Mission, PEOs, POs, PSOs, Syllabus, Mapping & Intro to SQL"
    },
    {
        "id": "sec-week-1",
        "num": "01",
        "badge": "EXP-01",
        "title": "Week 1: Concept Design with E-R Model",
        "short_title": "W01: ER Model",
        "co": "CO1",
        "desc": "Entities, Attributes, Keys, Cardinality, ER Diagrams, Relational Schema & Tables"
    },
    {
        "id": "sec-week-2",
        "num": "02",
        "badge": "EXP-02",
        "title": "Week 2: Database Normalization (1NF, 2NF, 3NF)",
        "short_title": "W02: Normalization",
        "co": "CO1",
        "desc": "1NF, 2NF, 3NF Normalization on Passenger, Bus, and Ticket entities"
    },
    {
        "id": "sec-week-3",
        "num": "03",
        "badge": "EXP-03",
        "title": "Week 3: MySQL Setup & DDL Commands",
        "short_title": "W03: DDL & MySQL",
        "co": "CO3",
        "desc": "MySQL 5.0 setup, CREATE, ALTER, DROP, RENAME, TRUNCATE & Roadway Travels schema"
    },
    {
        "id": "sec-week-4",
        "num": "04",
        "badge": "EXP-04",
        "title": "Week 4: Practicing DML Commands",
        "short_title": "W04: DML Commands",
        "co": "CO2",
        "desc": "INSERT, SELECT, UPDATE, DELETE commands with complete sample data tables"
    },
    {
        "id": "sec-week-5",
        "num": "05",
        "badge": "EXP-05",
        "title": "Week 5: Creation and Implementation of Constraints",
        "short_title": "W05: Constraints",
        "co": "CO2",
        "desc": "UNIQUE, PRIMARY KEY, NOT NULL, FOREIGN KEY constraints & error tests"
    },
    {
        "id": "sec-week-6",
        "num": "06",
        "badge": "EXP-06",
        "title": "Week 6: Querying (ANY, ALL, UNION, INTERSECT)",
        "short_title": "W06: Queries",
        "co": "CO4",
        "desc": "10 queries using ANY, ALL, IN, LIKE, ORDER BY, TIMEDIFF, subqueries"
    },
    {
        "id": "sec-week-7",
        "num": "07",
        "badge": "EXP-07",
        "title": "Week 7: Querying using Joins (Inner, Left, Right, Full)",
        "short_title": "W07: Joins",
        "co": "CO5",
        "desc": "INNER JOIN, LEFT JOIN, RIGHT JOIN (2 & 3 tables) and FULL OUTER JOIN via UNION"
    },
    {
        "id": "sec-week-8",
        "num": "08",
        "badge": "EXP-08",
        "title": "Week 8: Nested & Correlated Subqueries",
        "short_title": "W08: Subqueries",
        "co": "CO4",
        "desc": "Nested (ANY, ALL, EXISTS, NOT EXISTS) and Correlated subqueries (AVG, EXISTS)"
    },
    {
        "id": "sec-week-9",
        "num": "09",
        "badge": "EXP-09",
        "title": "Week 9: Aggregate Functions, GROUP BY, HAVING & Views",
        "short_title": "W09: Aggregates",
        "co": "CO4",
        "desc": "COUNT, SUM, AVG, MAX, MIN, GROUP BY, HAVING & Views creation/drop"
    },
    {
        "id": "sec-week-10",
        "num": "10",
        "badge": "EXP-10",
        "title": "Week 10: Database Triggers (Insert, Delete, Update)",
        "short_title": "W10: Triggers",
        "co": "CO5",
        "desc": "BEFORE UPDATE (t1), BEFORE INSERT (t3), BEFORE DELETE (rc) with tests"
    },
    {
        "id": "sec-week-11",
        "num": "11",
        "badge": "EXP-11",
        "title": "Week 11: Stored Procedures",
        "short_title": "W11: Procedures",
        "co": "CO3",
        "desc": "Stored procedures p2 (age threshold), p3 (timediff > 10 hours) & CALL"
    },
    {
        "id": "sec-week-12",
        "num": "12",
        "badge": "EXP-12",
        "title": "Week 12: Database Cursors",
        "short_title": "W12: Cursors",
        "co": "CO3",
        "desc": "DECLARE, OPEN, FETCH, CLOSE syntax and execution of mycur1 & mycur5"
    },
    {
        "id": "sec-raw-doc",
        "num": "RAW",
        "badge": "VERBATIM",
        "title": "Raw Document Verbatim Copy (At Last)",
        "short_title": "RAW DOCUMENT",
        "co": "ALL",
        "desc": "Complete, exact raw plaintext file (79,560 characters) - automatically copied on open"
    }
]

print("Metadata configured.")

