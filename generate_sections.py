# -*- coding: utf-8 -*-
"""
generate_sections.py
Generates the HTML content for all 13 sections of the lab manual.
"""

import html
import re

def build_overview_html():
    return '''
    <section id="sec-overview" class="lab-section active" data-week="overview">
        <div class="terminal-banner">
            <pre class="ascii-art">
 ██╗   ██╗██████╗ ██╗████████╗    ██████╗ ██████╗ ███╗   ███╗███████╗
 ██║   ██║██╔══██╗██║╚══██╔══╝    ██╔══██╗██╔══██╗████╗ ████║██╔════╝
 ██║   ██║██████╔╝██║   ██║       ██║  ██║██████╔╝██╔████╔██║███████╗
 ╚██╗ ██╔╝██╔══██╗██║   ██║       ██║  ██║██╔══██╗██║╚██╔╝██║╚════██║
  ╚████╔╝ ██████╔╝██║   ██║       ██████╔╝██████╔╝██║ ╚═╝ ██║███████║
   ╚═══╝  ╚═════╝ ╚═╝   ╚═╝       ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
 [ DATABASE MANAGEMENT SYSTEMS LAB MANUAL :: B.TECH II YEAR - I SEM ]
            </pre>
        </div>

        <div class="college-info-card terminal-card">
            <div class="college-header-content">
                <div class="college-logo-wrapper">
                    <img src="images/image1.jpeg" alt="Vignana Bharathi Institute of Technology Logo" class="college-logo-img">
                </div>
                <div class="college-details">
                    <h2 class="college-name">VIGNANA BHARATHI INSTITUTE OF TECHNOLOGY</h2>
                    <p class="college-sub">(A UGC Autonomous Institution, Approved by AICTE, Accredited by NBA & NAAC-A Grade, Affiliated to JNTUH)</p>
                    <p class="college-code">Counselling Code: <strong>VBIT</strong></p>
                    <div class="dept-badge">DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING [AI & ML]</div>
                    <h3 class="manual-title">STUDENT LAB MANUAL :: DATABASE MANAGEMENT SYSTEMS LAB</h3>
                    <p class="manual-meta">B.Tech II Year – I SEM | Course Code: <strong>25CS2153</strong> | Credits: <strong>1 (L:0, T:0, P:2)</strong></p>
                    <p class="faculty-credit">Prepared by: <strong>Azra Fathima</strong>, Asst. Professor, CSE (AI & ML) Department</p>
                </div>
            </div>
        </div>

        <div class="guidelines-card terminal-card">
            <div class="card-header">
                <span class="step-badge">PROTOCOL</span>
                <span class="card-title">GUIDELINES TO STUDENTS</span>
            </div>
            <ul class="terminal-list">
                <li><span class="list-bullet">▶</span> Equipment in the lab is for the use of the student community. Students need to maintain proper decorum in the computer lab. They must use the equipment with care. Any damage caused is punishable.</li>
                <li><span class="list-bullet">▶</span> Students are instructed to come to the lab in <strong>formal dress only</strong>.</li>
                <li><span class="list-bullet">▶</span> Students are supposed to occupy the systems allotted to them and should not talk or make noise in the lab.</li>
                <li><span class="list-bullet">▶</span> Students are required to carry their <strong>observation book</strong> and <strong>lab records with completed exercises</strong> while entering the lab.</li>
                <li><span class="list-bullet">▶</span> <strong>Lab records need to be submitted every week.</strong></li>
                <li><span class="list-bullet">▶</span> Students are <strong>not supposed to use pen drives</strong> in the lab.</li>
            </ul>
        </div>

        <div class="grid-2-col">
            <div class="terminal-card">
                <div class="card-header">
                    <span class="step-badge">VISION & MISSION</span>
                    <span class="card-title">DEPARTMENT OF CSE (AI & ML)</span>
                </div>
                <h4 class="term-subtitle">Vision</h4>
                <p class="term-text">To achieve global standards of quality in technical education with the help of advanced resources and automated tools to bridge the gap between industry and academia.</p>
                <h4 class="term-subtitle">Mission</h4>
                <ul class="terminal-list">
                    <li><span class="list-bullet">✓</span> Build the students technically competent on the global arena through effective teaching-learning process and world-class infrastructure.</li>
                    <li><span class="list-bullet">✓</span> Inculcate professional ethics, societal concerns, technical skills, and life-long learning to succeed in multidisciplinary fields.</li>
                    <li><span class="list-bullet">✓</span> Establish a competency centre in the field of Artificial Intelligence and Machine Learning with the collaboration of industry and innovative research.</li>
                </ul>
            </div>

            <div class="terminal-card">
                <div class="card-header">
                    <span class="step-badge">OBJECTIVES</span>
                    <span class="card-title">PROGRAM EDUCATIONAL OBJECTIVES (PEOs)</span>
                </div>
                <ul class="terminal-list">
                    <li><strong>PEO1: Domain Knowledge</strong> - Impart a strong foundation in basic sciences, mathematics, engineering, and emerging areas using advanced tools and technologies.</li>
                    <li><strong>PEO2: Professional Employment</strong> - Develop professional skills that prepare students for immediate employment in industry, government, entrepreneurship, and research.</li>
                    <li><strong>PEO3: Higher Degrees</strong> - Encourage students to pursue higher studies and acquire master's and research degrees.</li>
                    <li><strong>PEO4: Engineering Citizenship</strong> - Communicate and work effectively, engage in teamwork, exhibit leadership skills, and maintain an ethical attitude with social responsibility.</li>
                    <li><strong>PEO5: Life Long Learning</strong> - Lead in their field and respond to the challenges of an ever-changing environment with current knowledge and technology.</li>
                </ul>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">SYLLABUS</span>
                <span class="card-title">COURSE OUTCOMES & EXPERIMENTS INDEX</span>
            </div>
            <div class="terminal-table-wrapper">
                <table class="terminal-grid-table">
                    <thead>
                        <tr>
                            <th>S.No</th>
                            <th>Name of the Experiment / Program</th>
                            <th>Course Outcome</th>
                            <th>Quick Nav</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>Concept design with E-R Model</td><td><span class="co-tag">CO1</span></td><td><button class="btn-jump" onclick="jumpToSection('week-1')">Open W01</button></td></tr>
                        <tr><td>2</td><td>Database Normalization (1NF, 2NF, 3NF)</td><td><span class="co-tag">CO1</span></td><td><button class="btn-jump" onclick="jumpToSection('week-2')">Open W02</button></td></tr>
                        <tr><td>3</td><td>Practicing DDL commands & MySQL Installation</td><td><span class="co-tag">CO3</span></td><td><button class="btn-jump" onclick="jumpToSection('week-3')">Open W03</button></td></tr>
                        <tr><td>4</td><td>Practicing DML commands</td><td><span class="co-tag">CO2</span></td><td><button class="btn-jump" onclick="jumpToSection('week-4')">Open W04</button></td></tr>
                        <tr><td>5</td><td>Creation and Implementation of Constraints</td><td><span class="co-tag">CO2</span></td><td><button class="btn-jump" onclick="jumpToSection('week-5')">Open W05</button></td></tr>
                        <tr><td>6</td><td>Querying (using ANY, ALL, UNION, INTERSECT)</td><td><span class="co-tag">CO4</span></td><td><button class="btn-jump" onclick="jumpToSection('week-6')">Open W06</button></td></tr>
                        <tr><td>7</td><td>Querying using Joins (Inner, Left, Right, Full)</td><td><span class="co-tag">CO5</span></td><td><button class="btn-jump" onclick="jumpToSection('week-7')">Open W07</button></td></tr>
                        <tr><td>8</td><td>Nested, Correlated subqueries</td><td><span class="co-tag">CO4</span></td><td><button class="btn-jump" onclick="jumpToSection('week-8')">Open W08</button></td></tr>
                        <tr><td>9</td><td>Queries using Aggregate functions, GROUP BY, HAVING & Views</td><td><span class="co-tag">CO4</span></td><td><button class="btn-jump" onclick="jumpToSection('week-9')">Open W09</button></td></tr>
                        <tr><td>10</td><td>Triggers (Creation of insert, delete, update trigger)</td><td><span class="co-tag">CO5</span></td><td><button class="btn-jump" onclick="jumpToSection('week-10')">Open W10</button></td></tr>
                        <tr><td>11</td><td>Procedures</td><td><span class="co-tag">CO3</span></td><td><button class="btn-jump" onclick="jumpToSection('week-11')">Open W11</button></td></tr>
                        <tr><td>12</td><td>Usage of Cursors</td><td><span class="co-tag">CO3</span></td><td><button class="btn-jump" onclick="jumpToSection('week-12')">Open W12</button></td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">FOUNDATION</span>
                <span class="card-title">INTRODUCTION TO SQL & ORACLE / MYSQL SUBSETS</span>
            </div>
            <div class="grid-2-col">
                <div class="sub-card">
                    <h4 class="term-subtitle">DDL (Data Definition Language)</h4>
                    <p class="term-text">Statements used to define the database structure or schema.</p>
                    <p><code>CREATE</code> - create objects in the database<br>
                    <code>ALTER</code> - alters the structure of the database<br>
                    <code>DROP</code> - delete objects from the database<br>
                    <code>TRUNCATE</code> - remove all records from a table (frees space)<br>
                    <code>RENAME</code> - rename an object</p>
                </div>
                <div class="sub-card">
                    <h4 class="term-subtitle">DML (Data Manipulation Language)</h4>
                    <p class="term-text">Statements for managing and manipulating data within schema objects.</p>
                    <p><code>INSERT</code> - insert data into a table<br>
                    <code>UPDATE</code> - updates existing data within a table<br>
                    <code>DELETE</code> - deletes records from a table (space remains)<br>
                    <code>SELECT</code> - retrieve data from the database</p>
                </div>
                <div class="sub-card">
                    <h4 class="term-subtitle">DCL (Data Control Language)</h4>
                    <p class="term-text">Statements used to create roles, permissions, and security control.</p>
                    <p><code>GRANT</code> - gives user's access privileges to database<br>
                    <code>REVOKE</code> - withdraw access privileges given with GRANT</p>
                </div>
                <div class="sub-card">
                    <h4 class="term-subtitle">TCL (Transaction Control Language)</h4>
                    <p class="term-text">Statements used to manage changes made by DML statements into logical transactions.</p>
                    <p><code>COMMIT</code> - save work done permanently<br>
                    <code>SAVEPOINT</code> - identify a point to which you can later roll back<br>
                    <code>ROLLBACK</code> - restore database to original since last COMMIT</p>
                </div>
            </div>
        </div>
    </section>
    '''

print("build_overview_html ready.")

