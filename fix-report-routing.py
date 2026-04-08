import os, shutil, subprocess

# Remove vercel.json - it's causing build failures
if os.path.exists("vercel.json"):
    os.remove("vercel.json")
    print("Removed vercel.json")

# Create report folder with index.html inside
# Vercel serves /report/ from report/index.html natively
os.makedirs("report", exist_ok=True)

# Copy report.html into report/index.html
if os.path.exists("report.html"):
    shutil.copy("report.html", "report/index.html")
    print("Copied report.html -> report/index.html")
else:
    print("ERROR: report.html not found")
    exit(1)

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "fix: report page as folder/index.html, remove vercel.json"])
subprocess.run(["git", "push"])
print("Done - wait 30s then visit /report/")