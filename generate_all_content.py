# -*- coding: utf-8 -*-
"""
generate_all_content.py
Constructs all week sections HTML with exact SQL, tables, outputs, and diagrams.
"""

from build_all_sections import make_sql_card, make_week_header
import html
import re

def build_week1_html():
    header = make_week_header(
        "week-1", "01", "Week 1: Concept Design with E-R Model", "CO1",
        "Analyze real-world problem domains, identify entities, attributes, primary/candidate/partial keys, establish relationships, specify cardinalities, and map conceptual ER diagrams into relational schemas for the 'Roadway Travels' application."
    )
    
    return f'''
    <section id="sec-week-1" class="lab-section" data-week="week-1">
        {header}

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">THEORY</span>
                <span class="card-title">E-R MODEL CONCEPTS & CORE DEFINITIONS</span>
            </div>
            <p class="term-text">Analyze the problem carefully and come up with entities in it. Identify what data has to be persisted in the database. This contains the entities, attributes, keys, and relationships.</p>
            
            <div class="term-def-grid">
                <div class="def-box">
                    <span class="def-term">Entity</span>
                    <span class="def-desc">An object in the real world with an independent existence (e.g., Passenger, Bus, Ticket).</span>
                    <div class="diagram-box">
                        <img src="images/image2.jpeg" alt="Entity representation" class="term-img">
                    </div>
                </div>
                <div class="def-box">
                    <span class="def-term">ER-Model & Relationships</span>
                    <span class="def-desc">Describes data as entities, relationships and attributes. An association among two or more entities.</span>
                    <div class="diagram-box">
                        <img src="images/image3.jpeg" alt="Relationship representation" class="term-img">
                    </div>
                </div>
                <div class="def-box">
                    <span class="def-term">Attributes</span>
                    <span class="def-desc">Properties characterizing an entity set (data items / fields). e.g., Busno, Source, Destination for Bus.</span>
                    <div class="diagram-box">
                        <img src="images/image4.jpeg" alt="Attributes representation" class="term-img">
                    </div>
                </div>
                <div class="def-box">
                    <span class="def-term">Primary & Candidate Keys</span>
                    <span class="def-desc">Minimal super key uniquely identifying each record. Underlined in ER diagrams.</span>
                    <div class="diagram-box">
                        <img src="images/image5.jpeg" alt="Keys representation" class="term-img">
                    </div>
                </div>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">CASE STUDY</span>
                <span class="card-title">"ROADWAY TRAVELS" ENTITY SPECIFICATIONS & SCHEMAS</span>
            </div>
            <div class="entity-spec-grid">
                <div class="entity-spec-box">
                    <h4 class="term-subtitle">1. Bus Entity</h4>
                    <p class="term-code-inline"><strong>Attributes:</strong> Busno, serviceno, source, destination, deptime, retime, bustype, noofseats</p>
                    <p class="term-code-inline"><strong>Candidate / Primary Key:</strong> (Busno, serviceno)</p>
                    <div class="diagram-box">
                        <img src="images/image13.jpeg" alt="Bus Entity Diagram" class="term-img">
                    </div>
                </div>
                <div class="entity-spec-box">
                    <h4 class="term-subtitle">2. Ticket Entity</h4>
                    <p class="term-code-inline"><strong>Attributes:</strong> Ticketno, joudate, joutime, source, destination, seatno, amount, catcard</p>
                    <p class="term-code-inline"><strong>Primary Key:</strong> Ticketno</p>
                    <div class="diagram-box">
                        <img src="images/image14.jpeg" alt="Ticket Entity Diagram" class="term-img">
                    </div>
                </div>
                <div class="entity-spec-box">
                    <h4 class="term-subtitle">3. Passenger Entity</h4>
                    <p class="term-code-inline"><strong>Attributes:</strong> Pnrno, pname, age, sex, ticketno, address, phno, catno</p>
                    <p class="term-code-inline"><strong>Primary Key:</strong> Pnrno</p>
                    <div class="diagram-box">
                        <img src="images/image15.jpeg" alt="Passenger Entity Diagram" class="term-img">
                    </div>
                </div>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">RELATIONSHIPS</span>
                <span class="card-title">CARDINALITY RATIOS & PARTICIPATION</span>
            </div>
            <div class="card-content-grid">
                <div class="card-sub-item">
                    <h4 class="term-subtitle">Bus & Ticket (1:M Binary Relationship)</h4>
                    <p class="term-text">One bus contains multiple tickets issued for a journey.</p>
                    <img src="images/image6.jpeg" alt="1 to M Bus contains Ticket" class="term-img">
                </div>
                <div class="card-sub-item">
                    <h4 class="term-subtitle">Passenger & Bus (M:1 Binary Relationship)</h4>
                    <p class="term-text">Many passengers travel in one designated bus (Total Participation).</p>
                    <img src="images/image7.jpeg" alt="M to 1 Passenger travels in Bus" class="term-img">
                </div>
                <div class="card-sub-item">
                    <h4 class="term-subtitle">Passenger & Ticket (M:N Binary Relationship)</h4>
                    <p class="term-text">Passenger reserves or cancels tickets. Reservation and cancellation are distinct relationship sets.</p>
                    <img src="images/image8.jpeg" alt="Reserves and Cancels" class="term-img">
                </div>
                <div class="card-sub-item">
                    <h4 class="term-subtitle">Total vs Partial Participation</h4>
                    <p class="term-text">Total participation: Every passenger entity must be related to a bus via travels relationship (double line). Partial participation: Only some passengers cancel tickets.</p>
                    <img src="images/image9.jpeg" alt="Total vs Partial Participation" class="term-img">
                </div>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">ADVANCED CONCEPTS</span>
                <span class="card-title">GENERALIZATION, AGGREGATION & SPECIALIZATION</span>
            </div>
            <div class="diagram-row">
                <div class="diagram-col">
                    <h4 class="term-subtitle">Generalization (Ticket ISA Fullticket / Halfticket)</h4>
                    <img src="images/image16.jpeg" alt="Generalization diagram" class="term-img">
                </div>
                <div class="diagram-col">
                    <h4 class="term-subtitle">Aggregation (Passenger travels in [Bus contains Ticket])</h4>
                    <img src="images/image17.jpeg" alt="Aggregation diagram" class="term-img">
                </div>
                <div class="diagram-col">
                    <h4 class="term-subtitle">Specialization (Senior Citizen, Physically Challenged, General)</h4>
                    <img src="images/image18.jpeg" alt="Specialization diagram" class="term-img">
                </div>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">ATTRIBUTE TYPES</span>
                <span class="card-title">COMPOSITE, MULTIVALUED & DERIVED ATTRIBUTES</span>
            </div>
            <div class="diagram-row">
                <div class="diagram-col">
                    <h4 class="term-subtitle">Composite (Address: Street, City, State)</h4>
                    <img src="images/image19.jpeg" alt="Composite attribute" class="term-img">
                </div>
                <div class="diagram-col">
                    <h4 class="term-subtitle">Multivalued (Bustype: Garuda, Luxury, Express)</h4>
                    <img src="images/image20.jpeg" alt="Multivalued attribute" class="term-img">
                </div>
                <div class="diagram-col">
                    <h4 class="term-subtitle">Derived (Age derived from DOB)</h4>
                    <img src="images/image21.jpeg" alt="Derived attribute" class="term-img">
                </div>
            </div>
        </div>

        <div class="terminal-card">
            <div class="card-header">
                <span class="step-badge">RELATIONAL TABLES</span>
                <span class="card-title">RELATIONAL SCHEMAS & SAMPLE POPULATED TABLES</span>
            </div>
            
            <h4 class="term-subtitle">Bus Relation</h4>
            <pre class="ascii-output"><code>Bus(Busno:numeric, serviceno:numeric, source:varchar(10), destination:varchar(10), deptime:time, retime:time, bustype:varchar(10), noofseats:int)

+--------+-----------+--------+-------------+----------+----------+---------+-----------+
| Busno  | serviceno | source | destination | deptime  | retime   | bustype | Noofseats |
+--------+-----------+--------+-------------+----------+----------+---------+-----------+
| Ap555  | 3889      | Srpt   | Hyd         | 9:00:00  | 19:15:00 | Ac      | 36        |
| Ap501  | 3891      | Srpt   | Hyd         | 10:00:15 | 20:15:00 | Ac      | 36        |
| Ap444  | 3601      | Hyd    | Srpt        | 9:00:00  | 19:30:00 | Nonac   | 52        |
| Ap891  | 3555      | Hyd    | Srpt        | 9:30:00  | 20:30:00 | Nonac   | 52        |
| Ap8830 | 3239      | Hyd    | Vij         | 9:00:00  | 22:30:00 | Metro   | 45        |
+--------+-----------+--------+-------------+----------+----------+---------+-----------+</code></pre>

            <h4 class="term-subtitle">Ticket Relation</h4>
            <pre class="ascii-output"><code>Ticket(Ticketno:numeric, joudate:date, joutime:time, source:varchar(10), destination:varchar(10), seatno:int(4), amount:decimal(10,3), catcard:char(3))

+----------+-----------+----------+--------+-------------+--------+--------+---------+
| Ticketno | Joudate   | Joutime  | Source | Destination | Seatno | Amount | Catcard |
+----------+-----------+----------+--------+-------------+--------+--------+---------+
| 1111     | 2010-8-5  | 9:00:00  | Srpt   | Hyd         | 5      | 96     | No      |
| 2222     | 2010-8-5  | 10:00:15 | Srpt   | Hyd         | 10     | 88     | Yes     |
| 3333     | 2010-8-15 | 9:00:00  | Hyd    | Srpt        | 15     | 88     | Yes     |
| 4444     | 2010-8-18 | 9:30:00  | Hyd    | Srpt        | 20     | 96     | No      |
| 5555     | 2010-8-6  | 9:00:00  | Hyd    | Vij         | 18     | 172    | Yes     |
+----------+-----------+----------+--------+-------------+--------+--------+---------+</code></pre>

            <h4 class="term-subtitle">Passenger Relation</h4>
            <pre class="ascii-output"><code>Passenger(Pnrno:numeric, pname:varchar(15), age:int(4), sex:char(3), ticketno:numeric, address:varchar(50), phno:numeric(10), catno:varchar(10))

+-------+---------+-----+-----+----------+----------+------------+---------+
| Pnrno | pname   | age | sex | ticketno | address  | phno       | Catno   |
+-------+---------+-----+-----+----------+----------+------------+---------+
| 1001  | Subbu   | 31  | M   | 1111     | 5-4,srpt | 9492506282 | Cap5112 |
| 1002  | Achaith | 22  | M   | 2222     | 6-8,hyd  | 9949060540 | Cap6900 |
| 1003  | Padma   | 25  | F   | 3333     | h/7,vij  | 9704054050 | Cap5772 |
| 1004  | Ravi    | 23  | M   | 4444     | 8-9,hyd  | 9704613151 | Cap6132 |
| 1005  | Satyam  | 42  | F   | 5555     | 9-11,hyd | 9848354941 | Cap6732 |
+-------+---------+-----+-----+----------+----------+------------+---------+</code></pre>

            <h4 class="term-subtitle">Reserves Relation</h4>
            <pre class="ascii-output"><code>Reserves(pnrno:numeric, joudate:date, noofseats:int(4), address:varchar(50), contact_no:numeric(10), status:char(3))

+-------+-----------+-----------+---------------+------------+--------+
| Pnrno | Joudate   | Noofseats | Address       | Contact_no | Status |
+-------+-----------+-----------+---------------+------------+--------+
| 1001  | 2010-8-5  | 10        | 5-4,srpt      | 9492506282 | Yes    |
| 1001  | 2010-8-15 | 5         | 5-4,srpt      | 9492506282 | Yes    |
| 1002  | 2010-8-5  | 5         | 6-8,hyd       | 9949060540 | Yes    |
| 1003  | 2010-8-15 | 6         | h/7,vij       | 9704054050 | Yes    |
| 1004  | 2010-8-18 | 8         | 8-9,hyd       | 9704613151 | Yes    |
| 1005  | 2010-8-5  | 9         | 9-11,hyd      | 9848354941 | No     |
| 1005  | 2010-8-6  | 5         | 9-11,hyd      | 9848354941 | Yes    |
+-------+-----------+-----------+---------------+------------+--------+</code></pre>

            <h4 class="term-subtitle">Cancels Relation</h4>
            <pre class="ascii-output"><code>Cancels(pnrno:numeric, joudate:date, noofseats:int(4), address:varchar(50), contact_no:numeric(10), status:char(3))

+-------+-----------+-----------+----------+------------+--------+
| Pnrno | Joudate   | Noofseats | Address  | Contact_no | Status |
+-------+-----------+-----------+----------+------------+--------+
| 1001  | 2010-8-5  | 5         | 5-4,srpt | 9492506282 | Yes    |
| 1002  | 2010-8-5  | 2         | 6-8,hyd  | 9949060540 | No     |
| 1003  | 2010-8-15 | 2         | h/7,vij  | 9704054050 | Yes    |
| 1004  | 2010-8-18 | 5         | 8-9,hyd  | 9704613151 | Yes    |
| 1005  | 2010-8-6  | 4         | 9-11,hyd | 9848354941 | Yes    |
+-------+-----------+-----------+----------+------------+--------+</code></pre>
        </div>
    </section>
    '''

print("build_week1_html ready.")

