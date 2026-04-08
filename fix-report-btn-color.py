import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<a href="/report" style="padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;border:1.5px solid rgba(255,255,255,.28);background:rgba(255,255,255,.06);color:rgba(255,255,255,.65);cursor:pointer;transition:all .18s;flex-shrink:0;text-decoration:none">Research Report</a>',
    '<a href="/report" style="padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;border:1.5px solid #D85A3099;background:rgba(216,90,48,.15);color:#D85A30;cursor:pointer;transition:all .18s;flex-shrink:0;text-decoration:none">Research Report</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Research Report button updated to coral")
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'feat: Research Report button coral colour'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then refresh")