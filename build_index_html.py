# -*- coding: utf-8 -*-
"""
build_index_html.py
Assembles index.html with all 13 sections, sidebar, topbar, and CLI.
"""

from generate_sections import build_overview_html
from generate_all_content import build_week1_html
from generate_all_content_part2 import build_week2_html, build_week3_html
from generate_weeks_4_to_7 import build_week4_html, build_week5_html, build_week6_html, build_week7_html
from generate_weeks_8_to_12 import build_week8_html, build_week9_html, build_week10_html, build_week11_html, build_week12_html, build_raw_doc_html

with open('raw_manual.txt', 'r', encoding='utf-8') as f:
    RAW_MANUAL = f.read()

# Build HTML pieces
sec_overview = build_overview_html()
sec_w1 = build_week1_html()
sec_w2 = build_week2_html()
sec_w3 = build_week3_html()
sec_w4 = build_week4_html()
sec_w5 = build_week5_html()
sec_w6 = build_week6_html()
sec_w7 = build_week7_html()
sec_w8 = build_week8_html()
sec_w9 = build_week9_html()
sec_w10 = build_week10_html()
sec_w11 = build_week11_html()
sec_w12 = build_week12_html()
sec_raw = build_raw_doc_html(RAW_MANUAL)

INDEX_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VBIT CSE(AI&ML) :: DBMS Lab Manual (25CS2153) - Terminal Edition</title>
    <meta name="description" content="Database Management Systems Lab Manual for B.Tech II Year - I SEM, Vignana Bharathi Institute of Technology. Features terminal UI, instant week-by-week access, and automatic raw manual clipboard copy.">
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body class="theme-matrix crt-active">

    <!-- 1. TOP TERMINAL TITLEBAR -->
    <header class="terminal-window-header">
        <div class="window-controls">
            <span class="win-dot dot-red" title="Close" onclick="showTerminalToast('⚡ Terminal session locked in persistent offline mode.', 2000)"></span>
            <span class="win-dot dot-yellow" title="Minimize" onclick="showTerminalToast('⚡ Terminal active.', 1500)"></span>
            <span class="win-dot dot-green" title="Full Screen" onclick="document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen()"></span>
            <span class="window-title"><strong>vbit@dbms-lab</strong>: ~/25CS2153-manual <em>git:(main)</em></span>
        </div>
        <div class="window-status-group">
            <span class="status-badge-online"><span class="badge-pulse"></span> ONLINE</span>
            <div id="top-clipboard-status" class="clipboard-status-indicator pulse-green" onclick="copyFullRawDocument()" title="Click to copy full raw manual">
                📋 CLIPBOARD: COPIED ✔
            </div>
            <button id="btn-mode-toggle" class="btn-term" onclick="toggleViewMode()" title="Toggle Single Week Tabbed View vs Full Stream View">
                <span>📑 Mode: Single Week</span>
            </button>
            <button id="btn-crt-toggle" class="btn-term" title="Toggle retro CRT scanlines">
                📺 CRT: ON
            </button>
            <select id="theme-selector" class="select-term" title="Choose Terminal Color Scheme">
                <option value="theme-matrix">🟢 Matrix Green</option>
                <option value="theme-cyber">🔵 Cyber Neon</option>
                <option value="theme-amber">🟡 Amber CRT</option>
                <option value="theme-monokai">🟣 Monokai Pro</option>
                <option value="theme-slate">⚪ Slate Dark</option>
            </select>
            <span id="term-clock" style="color: var(--text-muted); font-size: 0.8rem; margin-left: 6px;">00:00:00</span>
        </div>
    </header>

    <!-- 2. QUICK WEEK DOCK (1-CLICK INSTANT ACCESS) -->
    <nav class="terminal-sub-header">
        <div class="quick-week-dock">
            <button class="dock-pill active" data-week="overview" onclick="jumpToSection('overview')">📁 00_Overview</button>
            <button class="dock-pill" data-week="week-1" onclick="jumpToSection('week-1')">W01: ER Model</button>
            <button class="dock-pill" data-week="week-2" onclick="jumpToSection('week-2')">W02: Normalization</button>
            <button class="dock-pill" data-week="week-3" onclick="jumpToSection('week-3')">W03: MySQL & DDL</button>
            <button class="dock-pill" data-week="week-4" onclick="jumpToSection('week-4')">W04: DML Commands</button>
            <button class="dock-pill" data-week="week-5" onclick="jumpToSection('week-5')">W05: Constraints</button>
            <button class="dock-pill" data-week="week-6" onclick="jumpToSection('week-6')">W06: Queries (10)</button>
            <button class="dock-pill" data-week="week-7" onclick="jumpToSection('week-7')">W07: Joins</button>
            <button class="dock-pill" data-week="week-8" onclick="jumpToSection('week-8')">W08: Subqueries</button>
            <button class="dock-pill" data-week="week-9" onclick="jumpToSection('week-9')">W09: Aggregates</button>
            <button class="dock-pill" data-week="week-10" onclick="jumpToSection('week-10')">W10: Triggers</button>
            <button class="dock-pill" data-week="week-11" onclick="jumpToSection('week-11')">W11: Procedures</button>
            <button class="dock-pill" data-week="week-12" onclick="jumpToSection('week-12')">W12: Cursors</button>
            <button class="dock-pill dock-pill-raw" data-week="raw-doc" onclick="jumpToSection('raw-doc')">📄 13_RAW DOCUMENT</button>
        </div>
        <div class="header-action-tools">
            <button class="btn-term btn-primary" onclick="copyFullRawDocument()" title="Copy entire raw manual text">
                <span class="btn-icon">📋</span> Copy Raw File
            </button>
        </div>
    </nav>

    <!-- 3. MAIN TERMINAL WORKSPACE -->
    <div class="terminal-layout">

        <!-- SIDEBAR DIRECTORY TREE -->
        <aside class="terminal-sidebar">
            <div class="sidebar-header">
                <div class="search-box">
                    <span class="search-prompt">$ grep -i</span>
                    <input type="text" class="search-input" placeholder="Search queries, tables, weeks...">
                </div>
            </div>
            
            <ul class="tree-view">
                <li class="tree-header">EXPERIMENTS DIRECTORY</li>
                <li class="tree-item"><a href="#overview" class="tree-link active" data-week="overview" onclick="jumpToSection('overview')"><span>📁 00_Overview & Syllabus</span> <span class="tree-pill">INFO</span></a></li>
                <li class="tree-item"><a href="#week-1" class="tree-link" data-week="week-1" onclick="jumpToSection('week-1')"><span>📁 01_Week-1: E-R Model</span> <span class="tree-pill">CO1</span></a></li>
                <li class="tree-item"><a href="#week-2" class="tree-link" data-week="week-2" onclick="jumpToSection('week-2')"><span>📁 02_Week-2: Normalization</span> <span class="tree-pill">CO1</span></a></li>
                <li class="tree-item"><a href="#week-3" class="tree-link" data-week="week-3" onclick="jumpToSection('week-3')"><span>📁 03_Week-3: DDL & MySQL</span> <span class="tree-pill">CO3</span></a></li>
                <li class="tree-item"><a href="#week-4" class="tree-link" data-week="week-4" onclick="jumpToSection('week-4')"><span>📁 04_Week-4: DML Commands</span> <span class="tree-pill">CO2</span></a></li>
                <li class="tree-item"><a href="#week-5" class="tree-link" data-week="week-5" onclick="jumpToSection('week-5')"><span>📁 05_Week-5: Constraints</span> <span class="tree-pill">CO2</span></a></li>
                <li class="tree-item"><a href="#week-6" class="tree-link" data-week="week-6" onclick="jumpToSection('week-6')"><span>📁 06_Week-6: 10 Queries</span> <span class="tree-pill">CO4</span></a></li>
                <li class="tree-item"><a href="#week-7" class="tree-link" data-week="week-7" onclick="jumpToSection('week-7')"><span>📁 07_Week-7: Joins (Inner/Full)</span> <span class="tree-pill">CO5</span></a></li>
                <li class="tree-item"><a href="#week-8" class="tree-link" data-week="week-8" onclick="jumpToSection('week-8')"><span>📁 08_Week-8: Subqueries</span> <span class="tree-pill">CO4</span></a></li>
                <li class="tree-item"><a href="#week-9" class="tree-link" data-week="week-9" onclick="jumpToSection('week-9')"><span>📁 09_Week-9: Aggregates/Views</span> <span class="tree-pill">CO4</span></a></li>
                <li class="tree-item"><a href="#week-10" class="tree-link" data-week="week-10" onclick="jumpToSection('week-10')"><span>📁 10_Week-10: Triggers</span> <span class="tree-pill">CO5</span></a></li>
                <li class="tree-item"><a href="#week-11" class="tree-link" data-week="week-11" onclick="jumpToSection('week-11')"><span>📁 11_Week-11: Procedures</span> <span class="tree-pill">CO3</span></a></li>
                <li class="tree-item"><a href="#week-12" class="tree-link" data-week="week-12" onclick="jumpToSection('week-12')"><span>📁 12_Week-12: Cursors</span> <span class="tree-pill">CO3</span></a></li>
                <li class="tree-header" style="margin-top: 10px;">RAW DOCUMENT FILE</li>
                <li class="tree-item"><a href="#raw-doc" class="tree-link" data-week="raw-doc" onclick="jumpToSection('raw-doc')"><span>📄 13_raw_manual.txt</span> <span class="tree-pill" style="color:#ff007f; border-color:#ff007f;">AUTO</span></a></li>
            </ul>

            <div class="sidebar-footer-actions">
                <button class="btn-term btn-primary" onclick="copyFullRawDocument()">
                    <span class="btn-icon">📋</span> Copy Full Raw Manual
                </button>
                <button class="btn-term" onclick="downloadRawManual()">
                    <span class="btn-icon">💾</span> Download raw_manual.txt
                </button>
            </div>
        </aside>

        <!-- MAIN TERMINAL CONTENT CANVAS -->
        <main class="terminal-main-canvas">
            {sec_overview}
            {sec_w1}
            {sec_w2}
            {sec_w3}
            {sec_w4}
            {sec_w5}
            {sec_w6}
            {sec_w7}
            {sec_w8}
            {sec_w9}
            {sec_w10}
            {sec_w11}
            {sec_w12}
            {sec_raw}
        </main>
    </div>

    <!-- 4. BOTTOM INTERACTIVE CLI CONSOLE -->
    <footer class="terminal-cli-dock">
        <div id="cli-history" class="cli-history-window"></div>
        <div class="cli-bar">
            <span class="cli-prompt-label">vbit@dbms-lab:~$</span>
            <input type="text" id="cli-input" class="cli-input-field" placeholder="Terminal CLI :: Type 'help', 'ls', 'week 4', 'copy raw', 'theme cyber', 'clear'..." autocomplete="off" spellcheck="false">
            <button class="btn-term-sm" onclick="executeCommand('help')">Commands</button>
            <button class="btn-term-sm" onclick="executeCommand('ls')">ls</button>
            <button class="btn-term-sm" onclick="copyFullRawDocument()">Copy Raw</button>
        </div>
    </footer>

    <!-- TOAST NOTIFICATION CONTAINER -->
    <div id="terminal-toast" class="terminal-toast">
        <span class="toast-icon">⚡</span>
        <span class="toast-msg">Terminal ready</span>
    </div>

    <script src="app.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(INDEX_TEMPLATE)

print("index.html created successfully!")

