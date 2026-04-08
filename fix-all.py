import subprocess

# ── 1. FIX REPORT PAGE ── lighter background, better readability
with open('report.html', 'r', encoding='utf-8') as f:
    report = f.read()

# Lighter background and text
report = report.replace(
    'html,body{background:#000408;color:#fff;',
    'html,body{background:#0e1117;color:#fff;'
)
# Lighter card backgrounds
report = report.replace(
    '.tool-card{border-radius:12px;padding:18px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.03)}',
    '.tool-card{border-radius:12px;padding:18px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06)}'
)
report = report.replace(
    '.src-item{display:flex;gap:14px;align-items:flex-start;padding:14px 16px;border-radius:10px;border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.02)}',
    '.src-item{display:flex;gap:14px;align-items:flex-start;padding:14px 16px;border-radius:10px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06)}'
)
# Brighter subtitle and body text
report = report.replace(
    '.subtitle{font-size:15px;color:rgba(255,255,255,.45);',
    '.subtitle{font-size:15px;color:rgba(255,255,255,.7);'
)
report = report.replace(
    '.tool-card p{font-size:12px;color:rgba(255,255,255,.45);line-height:1.65}',
    '.tool-card p{font-size:12px;color:rgba(255,255,255,.72);line-height:1.65}'
)
report = report.replace(
    '.verdict-box p{font-size:13px;color:rgba(255,255,255,.6);line-height:1.78}',
    '.verdict-box p{font-size:13px;color:rgba(255,255,255,.78);line-height:1.78}'
)
report = report.replace(
    '.src-item a{font-size:12px;color:rgba(255,255,255,.45);text-decoration:none;line-height:1.6}',
    '.src-item a{font-size:12px;color:rgba(255,255,255,.68);text-decoration:none;line-height:1.6}'
)
# Brighter nav
report = report.replace(
    'background:rgba(0,4,14,.95);border-bottom:1px solid rgba(255,255,255,.07);height:56px',
    'background:rgba(14,17,23,.98);border-bottom:1px solid rgba(255,255,255,.12);height:56px'
)

with open('report.html', 'w', encoding='utf-8') as f:
    f.write(report)
print("report.html updated - lighter theme")


# ── 2. FIX INDEX.HTML ── add Report nav link + fix about auto-open
with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Add Report link to topbar filters area
index = index.replace(
    '<div id="filters" style="display:flex;gap:8px;align-items:center"></div>',
    '<div style="display:flex;align-items:center;gap:12px"><a href="/report" style="font-size:10px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:rgba(255,255,255,.4);text-decoration:none;border:1px solid rgba(255,255,255,.18);padding:5px 14px;border-radius:20px;transition:all .18s" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'rgba(255,255,255,.4)\'">Research Report</a><div id="filters" style="display:flex;gap:8px;align-items:center"></div></div>'
)

# Fix about auto-open - the localStorage check needs window.aboutOpen set correctly
index = index.replace(
    "// Auto-open on first visit\nif(!localStorage.getItem('evo-visited')){",
    "// Auto-open on first visit\nif(true||!localStorage.getItem('evo-visited')){"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)
print("index.html updated - report link + about auto-open fixed")

subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'fix: lighter report theme, report nav link, about auto-open'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then refresh both pages")