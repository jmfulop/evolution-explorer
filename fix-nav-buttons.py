import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the research report link we added in the filters area
html = html.replace(
    '<div style="display:flex;align-items:center;gap:12px"><a href="/report" style="font-size:10px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:rgba(255,255,255,.4);text-decoration:none;border:1px solid rgba(255,255,255,.18);padding:5px 14px;border-radius:20px;transition:all .18s" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'rgba(255,255,255,.4)\'">Research Report</a><div id="filters" style="display:flex;gap:8px;align-items:center"></div></div>',
    '<div id="filters" style="display:flex;gap:8px;align-items:center"></div>'
)

# Add Research Report button right next to About button, same exact style
html = html.replace(
    '<button id="about-btn" onclick="toggleAbout()" style="padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;border:1.5px solid #1D9E75;background:rgba(29,158,117,.15);color:#1D9E75;cursor:pointer;transition:all .18s;flex-shrink:0;animation:pulse-about 2s ease-in-out infinite">About</button>',
    '<button id="about-btn" onclick="toggleAbout()" style="padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;border:1.5px solid #1D9E75;background:rgba(29,158,117,.15);color:#1D9E75;cursor:pointer;transition:all .18s;flex-shrink:0;animation:pulse-about 2s ease-in-out infinite">About</button>\n      <a href="/report" style="padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;border:1.5px solid rgba(255,255,255,.28);background:rgba(255,255,255,.06);color:rgba(255,255,255,.65);cursor:pointer;transition:all .18s;flex-shrink:0;text-decoration:none">Research Report</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Nav buttons updated")
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'fix: Research Report button same size as About, next to it'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then refresh")