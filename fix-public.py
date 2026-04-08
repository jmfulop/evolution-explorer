import json, os, shutil, subprocess

# Remove the public folder - it's confusing Vercel into using it as webroot
if os.path.isdir('public'):
    shutil.rmtree('public')
    print("Removed public/ folder")

# Write vercel.json with explicit output directory and cleanUrls
config = {
    "outputDirectory": ".",
    "cleanUrls": True
}
with open('vercel.json', 'w', newline='\n') as f:
    json.dump(config, f, indent=2)
print("vercel.json:", open('vercel.json').read())

subprocess.run(['git', 'add', '-A'])
subprocess.run(['git', 'commit', '-m', 'fix: remove public folder, set outputDirectory to root'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then try the site")