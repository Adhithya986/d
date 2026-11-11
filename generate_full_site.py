# -*- coding: utf-8 -*-
"""
Full Site Generator for VBIT DBMS Lab Manual Terminal App
Creates:
  - index.html
  - styles.css
  - app.js
"""

import os
import re
import json
import html

# Load raw manual
with open('raw_manual.txt', 'r', encoding='utf-8') as f:
    RAW_MANUAL = f.read()

print(f"Loaded raw manual: {len(RAW_MANUAL)} chars")

def make_sql_card(step_badge, title, sql_code, output_text=None, note=None):
    clean_sql = re.sub(r'^(mysql>|SQL>|->)\s*', '', sql_code, flags=re.MULTILINE).strip()
    escaped_clean = html.escape(clean_sql)
    escaped_display = html.escape(sql_code)
    
    # Simple syntax highlighting
    keywords = [
        'SELECT', 'FROM', 'WHERE', 'INSERT INTO', 'INSERT', 'INTO', 'VALUES',
        'UPDATE', 'SET', 'DELETE FROM', 'DELETE', 'CREATE TABLE', 'CREATE DATABASE',
        'CREATE VIEW', 'CREATE PROCEDURE', 'CREATE TRIGGER', 'CREATE', 'TABLE',
        'ALTER TABLE', 'ALTER', 'ADD CONSTRAINT', 'ADD', 'DROP TABLE', 'DROP DATABASE',
        'DROP VIEW', 'DROP', 'RENAME TABLE', 'RENAME', 'TO', 'TRUNCATE TABLE', 'TRUNCATE',
        'DATABASE', 'DATABASES', 'SHOW', 'USE', 'DESC', 'PRIMARY KEY', 'PRIMARY', 'KEY',
        'FOREIGN KEY', 'FOREIGN', 'REFERENCES', 'UNIQUE', 'CHECK', 'NOT NULL', 'NOT',
        'NULL', 'DEFAULT', 'INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'JOIN', 'ON',
        'UNION', 'INTERSECT', 'ALL', 'ANY', 'IN', 'EXISTS', 'NOT EXISTS', 'LIKE',
        'BETWEEN', 'AND', 'OR', 'ORDER BY', 'GROUP BY', 'HAVING', 'COUNT', 'SUM',
        'AVG', 'MIN', 'MAX', 'AS', 'DISTINCT', 'TRIGGER', 'BEFORE', 'AFTER', 'FOR EACH ROW',
        'EACH', 'ROW', 'BEGIN', 'END', 'IF', 'THEN', 'ELSE', 'DELIMITER', 'PROCEDURE',
        'CALL', 'DECLARE', 'CURSOR FOR', 'CURSOR', 'OPEN', 'FETCH', 'CLOSE', 'VIEW',
        'TIMEDIFF', 'HOUR', 'DAYOFWEEK'
    ]
    for kw in sorted(keywords, key=len, reverse=True):
        pattern = r'\b(' + re.escape(kw) + r')\b'
        escaped_display = re.sub(pattern, r'<span class="kw">\1</span>', escaped_display, flags=re.IGNORECASE)
    
    escaped_display = re.sub(r"('(?:\\.|[^'])*')", r'<span class="str">\1</span>', escaped_display)
    escaped_display = re.sub(r'^(mysql&gt;|SQL&gt;|\-\&gt;)', r'<span class="prompt">\1</span>', escaped_display, flags=re.MULTILINE)
    
    output_html = ""
    if output_text:
        escaped_out = html.escape(output_text.strip())
        output_html = f'''
        <div class="terminal-output-container">
            <div class="output-header">
                <span class="output-label">OUTPUT // RESULTS</span>
                <span class="output-tag">mysql-cli</span>
            </div>
            <pre class="ascii-output"><code>{escaped_out}</code></pre>
        </div>'''
        
    note_html = ""
    if note:
        note_html = f'<div class="terminal-note"><span class="note-bullet">⚡ NOTE:</span> {html.escape(note)}</div>'

    return f'''
    <div class="query-card terminal-card" data-step="{html.escape(step_badge)}">
        <div class="card-header">
            <div class="card-title-group">
                <span class="step-badge">{html.escape(step_badge)}</span>
                <span class="card-title">{html.escape(title)}</span>
            </div>
            <button class="btn-term-sm copy-btn" data-copy="{escaped_clean}" title="Copy SQL command">
                <span class="btn-icon">📋</span> <span class="btn-text">Copy SQL</span>
            </button>
        </div>
        <div class="terminal-code-block">
            <div class="code-header">
                <span class="code-lang">SQL / MySQL 5.0+</span>
                <span class="code-status">READY</span>
            </div>
            <pre class="code-pre"><code>{escaped_display}</code></pre>
        </div>
        {output_html}
        {note_html}
    </div>'''

print("Card builder helper defined.")

