import os, shutil, json, subprocess

# 1. Remove everything that's breaking things
for f in ['vercel.json', 'report']:
    if os.path.isfile(f):
        os.remove(f)
        print(f"Removed file: {f}")
    elif os.path.isdir(f):
        shutil.rmtree(f)
        print(f"Removed folder: {f}")

# 2. Write correct vercel.json - cleanUrls serves report.html at /report
config = {"cleanUrls": True}
with open('vercel.json', 'w', newline='\n') as f:
    json.dump(config, f, indent=2)
print("Written vercel.json:", open('vercel.json').read())

# 3. Confirm index.html and report.html exist
for f in ['index.html', 'report.html']:
    if os.path.exists(f):
        print(f"OK: {f} exists")
    else:
        print(f"MISSING: {f} - this is a problem!")

# 4. Push
subprocess.run(['git', 'add', '-A'])
subprocess.run(['git', 'commit', '-m', 'fix: clean slate - remove report folder, cleanUrls only'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then try / and /report")