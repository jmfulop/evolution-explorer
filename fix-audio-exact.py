import subprocess

with open('report.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Exact text found in the file
old = ' NotebookLM from the research sources. Two AI hosts discuss the key findings, contested claims, and implications of the 2025 discoveries.</p>\n      <a class="audio-link" id="audio-link" href="https://notebooklm.google.com/notebook/c40aec28-3852-47ed-8e58-d57f31719273?artifactId=70b18625-063b-4b06-9edd-ce858aa671b5" target="_blank">Listen on NotebookLM \u2197</a>\n      <p class="audio-placeholder">Paste your NotebookLM share link \u2014 open your notebook, click Share on the Audio Overview, copy the link, and replace the href above in report.html</p>\n    </div>\n  </div>'

new = ' NotebookLM from the research sources. An AI host discusses the key findings, the two ancestral populations discovery, and the implications of conscious evolution.</p>\n    <iframe width="100%" height="120" scrolling="no" frameborder="no" allow="autoplay"\n      src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/jean-grey-262620260/taking_control_of_human_evolut&color=%231D9E75&inverse=true&auto_play=false&show_user=false&show_comments=false&show_reposts=false&show_teaser=false"\n      style="border-radius:10px;margin-top:12px">\n    </iframe>\n    </div>\n  </div>'

if old in html:
    html = html.replace(old, new)
    print("SUCCESS - audio section replaced with SoundCloud embed")
else:
    print("ERROR - exact text not found")

with open('report.html', 'w', encoding='utf-8') as f:
    f.write(html)

subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'fix: replace NotebookLM link with SoundCloud embed'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then check /report")