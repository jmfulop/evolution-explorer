import json, subprocess

config = {
    "rewrites": [
        {"source": "/report", "destination": "/report.html"}
    ]
}

with open("vercel.json", "w") as f:
    json.dump(config, f)

print("vercel.json written:")
print(open("vercel.json").read())

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "fix: vercel.json clean write"])
subprocess.run(["git", "push"])
print("Done")