// ==========================================================================
// VBIT DBMS LAB MANUAL - TERMINAL INTERACTIVE JAVASCRIPT
// ==========================================================================

// Global state
let currentTheme = localStorage.getItem('vbit_dbms_theme') || 'theme-matrix';
let crtActive = localStorage.getItem('vbit_crt_mode') !== 'false';
let currentMode = 'tabbed'; // 'tabbed' or 'stream'

// DOM ready
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initCRT();
    initClock();
    initNavigation();
    initSearch();
    initCopyButtons();
    initCLI();
    
    // Automatic Clipboard Copy on page open
    autoCopyRawDocumentOnOpen();
});

// --------------------------------------------------------------------------
// 1. AUTOMATIC CLIPBOARD COPY ON URL OPEN (Core requirement)
// --------------------------------------------------------------------------
async function autoCopyRawDocumentOnOpen() {
    console.log('[Terminal] Initializing automatic copy of raw manual on open...');
    let success = false;
    
    try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(RAW_MANUAL_TEXT);
            success = true;
            console.log('[Terminal] Auto-copy succeeded via navigator.clipboard.');
        }
    } catch (err) {
        console.warn('[Terminal] Direct clipboard access restricted without gesture:', err);
    }
    
    if (!success) {
        // Fallback using execCommand textarea
        try {
            const tempTa = document.createElement('textarea');
            tempTa.value = RAW_MANUAL_TEXT;
            tempTa.style.position = 'fixed';
            tempTa.style.left = '-9999px';
            tempTa.style.top = '0';
            document.body.appendChild(tempTa);
            tempTa.focus();
            tempTa.select();
            success = document.execCommand('copy');
            document.body.removeChild(tempTa);
            if (success) {
                console.log('[Terminal] Auto-copy succeeded via execCommand fallback.');
            }
        } catch (e) {
            console.warn('[Terminal] Fallback copy also restricted:', e);
        }
    }
    
    if (success) {
        showTerminalToast('📋 SUCCESS: Full Raw Lab Manual automatically copied to clipboard! (Ready to paste: Ctrl+V)', 5000);
        updateClipboardUIStatus(true);
    } else {
        // Armed fallback: Eagerly listen to the user's very first click or keydown anywhere on the page
        const triggerEagerCopy = async () => {
            try {
                await navigator.clipboard.writeText(RAW_MANUAL_TEXT);
                showTerminalToast('📋 SUCCESS: Full Raw Lab Manual automatically copied to clipboard! (Ready to paste: Ctrl+V)', 5000);
                updateClipboardUIStatus(true);
            } catch (err) {
                fallbackCopy(RAW_MANUAL_TEXT);
            }
            window.removeEventListener('click', triggerEagerCopy);
            window.removeEventListener('keydown', triggerEagerCopy);
            window.removeEventListener('touchstart', triggerEagerCopy);
        };
        
        window.addEventListener('click', triggerEagerCopy, { once: true });
        window.addEventListener('keydown', triggerEagerCopy, { once: true });
        window.addEventListener('touchstart', triggerEagerCopy, { once: true });
        
        showTerminalToast('📋 Auto-copy armed! Click anywhere to confirm copy to clipboard.', 4000);
    }
}

function updateClipboardUIStatus(copied) {
    const badge = document.getElementById('top-clipboard-status');
    const rawBadge = document.getElementById('raw-badge-status');
    if (badge) {
        badge.innerHTML = copied ? '📋 CLIPBOARD: COPIED ✔' : '📋 CLIPBOARD: READY';
        badge.classList.toggle('pulse-green', copied);
    }
    if (rawBadge) {
        rawBadge.innerHTML = copied ? '✔ AUTO-COPIED ON OPEN' : 'READY TO COPY';
    }
}

// --------------------------------------------------------------------------
// 2. COPY FUNCTIONS
// --------------------------------------------------------------------------
function copyFullRawDocument() {
    copyTextToClipboard(RAW_MANUAL_TEXT, 'Full Raw Lab Manual Document (79,560 characters) copied to clipboard!');
}

function copyWeekSQL(sqlCode) {
    copyTextToClipboard(sqlCode, 'Experiment SQL commands copied to clipboard!');
}

function copyTextToClipboard(text, successMsg) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            showTerminalToast(`✔ ${successMsg}`, 3000);
            updateClipboardUIStatus(true);
        }).catch(() => {
            fallbackCopy(text);
        });
    } else {
        fallbackCopy(text);
    }
}

function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try {
        document.execCommand('copy');
        showTerminalToast('✔ Copied to clipboard!', 3000);
        updateClipboardUIStatus(true);
    } catch (err) {
        showTerminalToast('✖ Unable to copy automatically. Please select text manually.', 3000);
    }
    document.body.removeChild(ta);
}

function downloadRawManual() {
    const blob = new Blob([RAW_MANUAL_TEXT], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'DBMS_LAB_MANUAL_2025-26_RAW.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showTerminalToast('💾 Downloading DBMS_LAB_MANUAL_2025-26_RAW.txt', 3000);
}

function selectRawText() {
    const pre = document.getElementById('raw-verbatim-text');
    if (pre) {
        const range = document.createRange();
        range.selectNodeContents(pre);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        showTerminalToast('📄 Raw manual text selected! Press Ctrl+C to copy.', 3000);
    }
}

// --------------------------------------------------------------------------
// 3. TOAST NOTIFICATIONS
// --------------------------------------------------------------------------
let toastTimer = null;
function showTerminalToast(message, duration = 3000) {
    let toast = document.getElementById('terminal-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'terminal-toast';
        toast.className = 'terminal-toast';
        document.body.appendChild(toast);
    }
    toast.innerHTML = `<span class="toast-icon">⚡</span> <span class="toast-msg">${message}</span>`;
    toast.classList.add('show');
    
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
        toast.classList.remove('show');
    }, duration);
}

// --------------------------------------------------------------------------
// 4. NAVIGATION & EXPERIMENT ACCESS
// --------------------------------------------------------------------------
function initNavigation() {
    // Check URL hash
    const hash = window.location.hash.replace('#', '');
    if (hash) {
        jumpToSection(hash);
    }
    
    // Copy buttons inside cards
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const sql = btn.getAttribute('data-copy');
            if (sql) {
                copyTextToClipboard(sql, 'SQL Query copied!');
                btn.innerHTML = '✔ Copied!';
                setTimeout(() => {
                    btn.innerHTML = '<span class="btn-icon">📋</span> <span class="btn-text">Copy SQL</span>';
                }, 1500);
            }
        });
    });
    
    // Copy entire week buttons
    document.querySelectorAll('.copy-week-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const sql = btn.getAttribute('data-copy');
            if (sql) {
                copyWeekSQL(sql);
                btn.innerHTML = '✔ All Week SQL Copied!';
                setTimeout(() => {
                    btn.innerHTML = '<span class="btn-icon">📋</span> Copy Entire Week SQL';
                }, 2000);
            }
        });
    });
}

function jumpToSection(weekId) {
    // Standardize id
    if (!weekId.startsWith('sec-')) {
        weekId = 'sec-' + weekId;
    }
    
    const targetSec = document.getElementById(weekId);
    if (!targetSec) return;
    
    if (currentMode === 'tabbed') {
        // Hide all sections, show active
        document.querySelectorAll('.lab-section').forEach(s => s.classList.remove('active'));
        targetSec.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        // Stream mode: scroll to section
        targetSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    
    // Update active pills
    const rawWeekKey = weekId.replace('sec-', '');
    document.querySelectorAll('.dock-pill').forEach(pill => {
        pill.classList.toggle('active', pill.getAttribute('data-week') === rawWeekKey);
    });
    
    document.querySelectorAll('.tree-link').forEach(link => {
        link.classList.toggle('active', link.getAttribute('data-week') === rawWeekKey);
    });
    
    window.location.hash = rawWeekKey;
}

function toggleViewMode() {
    const btn = document.getElementById('btn-mode-toggle');
    if (currentMode === 'tabbed') {
        currentMode = 'stream';
        document.body.classList.add('mode-stream');
        if (btn) btn.innerHTML = '<span>📜 Mode: Stream All</span>';
        showTerminalToast('📜 Switched to Full Manual Stream Mode (all weeks displayed)', 2500);
    } else {
        currentMode = 'tabbed';
        document.body.classList.remove('mode-stream');
        if (btn) btn.innerHTML = '<span>📑 Mode: Single Week</span>';
        showTerminalToast('📑 Switched to Single Week Focus Mode', 2500);
        // Ensure active section is visible
        const active = document.querySelector('.lab-section.active') || document.getElementById('sec-overview');
        if (active) jumpToSection(active.id);
    }
}

// --------------------------------------------------------------------------
// 5. SEARCH & FILTER
// --------------------------------------------------------------------------
function initSearch() {
    const searchInputs = document.querySelectorAll('.search-input');
    searchInputs.forEach(input => {
        input.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            filterContent(query);
        });
    });
}

function filterContent(query) {
    if (!query) {
        document.querySelectorAll('.query-card, .tree-item').forEach(el => el.style.display = '');
        return;
    }
    
    // Filter tree items in sidebar
    document.querySelectorAll('.tree-item').forEach(item => {
        const text = item.textContent.toLowerCase();
        item.style.display = text.includes(query) ? '' : 'none';
    });
    
    // Filter query cards in main view
    let matchCount = 0;
    document.querySelectorAll('.query-card').forEach(card => {
        const text = card.textContent.toLowerCase();
        const matches = text.includes(query);
        card.style.display = matches ? '' : 'none';
        if (matches) matchCount++;
    });
}

// --------------------------------------------------------------------------
// 6. THEMES & CRT EFFECTS
// --------------------------------------------------------------------------
function initTheme() {
    document.body.className = currentTheme;
    if (crtActive) document.body.classList.add('crt-active');
    
    const selector = document.getElementById('theme-selector');
    if (selector) {
        selector.value = currentTheme;
        selector.addEventListener('change', (e) => {
            setTheme(e.target.value);
        });
    }
}

function setTheme(themeName) {
    document.body.classList.remove('theme-matrix', 'theme-cyber', 'theme-amber', 'theme-monokai', 'theme-slate');
    document.body.classList.add(themeName);
    currentTheme = themeName;
    localStorage.setItem('vbit_dbms_theme', themeName);
    showTerminalToast(`🎨 Theme set to: ${themeName.replace('theme-', '').toUpperCase()}`, 2000);
}

function initCRT() {
    const btn = document.getElementById('btn-crt-toggle');
    if (btn) {
        btn.addEventListener('click', toggleCRT);
    }
}

function toggleCRT() {
    crtActive = !crtActive;
    document.body.classList.toggle('crt-active', crtActive);
    localStorage.setItem('vbit_crt_mode', crtActive);
    const btn = document.getElementById('btn-crt-toggle');
    if (btn) {
        btn.innerHTML = crtActive ? '📺 CRT: ON' : '📺 CRT: OFF';
    }
    showTerminalToast(crtActive ? '📺 CRT Scanlines Activated' : '📺 CRT Scanlines Deactivated', 2000);
}

// --------------------------------------------------------------------------
// 7. REAL-TIME CLOCK & UPTIME
// --------------------------------------------------------------------------
function initClock() {
    const clockEl = document.getElementById('term-clock');
    const updateTime = () => {
        if (clockEl) {
            const now = new Date();
            clockEl.textContent = now.toTimeString().split(' ')[0];
        }
    };
    updateTime();
    setInterval(updateTime, 1000);
}

// --------------------------------------------------------------------------
// 8. INTERACTIVE CLI CONSOLE
// --------------------------------------------------------------------------
function initCLI() {
    const input = document.getElementById('cli-input');
    const win = document.getElementById('cli-history');
    if (!input || !win) return;
    
    const history = [];
    let histIndex = -1;
    
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const cmd = input.value.trim();
            if (cmd) {
                history.push(cmd);
                histIndex = history.length;
                executeCommand(cmd);
                input.value = '';
            }
        } else if (e.key === 'ArrowUp') {
            if (histIndex > 0) {
                histIndex--;
                input.value = history[histIndex];
            }
        } else if (e.key === 'ArrowDown') {
            if (histIndex < history.length - 1) {
                histIndex++;
                input.value = history[histIndex];
            } else {
                histIndex = history.length;
                input.value = '';
            }
        }
    });
}

function executeCommand(cmd) {
    const win = document.getElementById('cli-history');
    if (!win) return;
    
    win.classList.add('open');
    const addLine = (text, type = 'out') => {
        const div = document.createElement('div');
        div.className = `cli-line cli-line-${type}`;
        div.innerHTML = text;
        win.appendChild(div);
        win.scrollTop = win.scrollHeight;
    };
    
    addLine(`vbit@dbms-lab:~$ ${html.escape(cmd)}`, 'user');
    const lower = cmd.toLowerCase();
    
    if (lower === 'help') {
        addLine(`Available commands:
  - <strong>ls</strong> / <strong>dir</strong>: list all weeks & experiments
  - <strong>cat week-&lt;N&gt;</strong> or <strong>week &lt;N&gt;</strong>: open specific week (1..12)
  - <strong>cat raw</strong> / <strong>raw</strong>: jump to raw verbatim manual
  - <strong>copy raw</strong>: copy entire raw manual to clipboard
  - <strong>copy week &lt;N&gt;</strong>: copy SQL for week N
  - <strong>theme &lt;matrix|cyber|amber|monokai|slate&gt;</strong>: switch UI theme
  - <strong>crt</strong>: toggle CRT scanlines
  - <strong>mode</strong>: toggle Single Week vs All Stream mode
  - <strong>clear</strong>: clear CLI history
  - <strong>whoami</strong>: display lab & student context`, 'out');
    } else if (lower === 'ls' || lower === 'dir') {
        addLine(`drwxr-xr-x 00_overview/
drwxr-xr-x 01_week-1_er-model/
drwxr-xr-x 02_week-2_normalization/
drwxr-xr-x 03_week-3_mysql-ddl/
drwxr-xr-x 04_week-4_dml-commands/
drwxr-xr-x 05_week-5_constraints/
drwxr-xr-x 06_week-6_querying/
drwxr-xr-x 07_week-7_joins/
drwxr-xr-x 08_week-8_subqueries/
drwxr-xr-x 09_week-9_aggregates-views/
drwxr-xr-x 10_week-10_triggers/
drwxr-xr-x 11_week-11_procedures/
drwxr-xr-x 12_week-12_cursors/
-rw-r--r-- 13_raw_manual_verbatim.txt (79,560 bytes)`, 'succ');
    } else if (lower === 'clear') {
        win.innerHTML = '';
        win.classList.remove('open');
    } else if (lower === 'copy raw') {
        copyFullRawDocument();
        addLine(`✔ Full raw manual copied to clipboard!`, 'succ');
    } else if (lower === 'cat raw' || lower === 'raw') {
        jumpToSection('raw-doc');
        addLine(`Opened section: RAW DOCUMENT VERBATIM COPY`, 'succ');
    } else if (lower.startsWith('week ') || lower.startsWith('cat week')) {
        const num = lower.replace(/^(week|cat week)[\s\-_]*/, '').trim();
        const weekKey = `week-${num}`;
        if (document.getElementById(`sec-${weekKey}`)) {
            jumpToSection(weekKey);
            addLine(`Navigated to Week ${num}`, 'succ');
        } else {
            addLine(`Error: Week ${num} not found. Available: 1 to 12.`, 'err');
        }
    } else if (lower.startsWith('theme ')) {
        const t = lower.split(' ')[1];
        if (['matrix', 'cyber', 'amber', 'monokai', 'slate'].includes(t)) {
            setTheme(`theme-${t}`);
            addLine(`Theme switched to ${t}`, 'succ');
        } else {
            addLine(`Unknown theme. Choose: matrix, cyber, amber, monokai, slate.`, 'err');
        }
    } else if (lower === 'crt') {
        toggleCRT();
        addLine(`CRT scanlines toggled`, 'succ');
    } else if (lower === 'mode') {
        toggleViewMode();
        addLine(`View mode toggled to: ${currentMode}`, 'succ');
    } else if (lower === 'whoami') {
        addLine(`student@vbit-cse-aiml :: Course: 25CS2153 DBMS LAB :: B.Tech II-I Sem`, 'succ');
    } else {
        addLine(`Command not recognized: '${html.escape(cmd)}'. Type 'help' for command list.`, 'err');
    }
}
