import os
import subprocess

commits = subprocess.check_output(['git', 'rev-list', '--count', 'HEAD']).decode().strip()
log_out = subprocess.check_output(['git', 'log', '--oneline']).decode('utf-8', errors='ignore')
merges = [l for l in log_out.splitlines() if 'merge' in l.lower()]
prs = [l for l in log_out.splitlines() if 'merge pull request #' in l.lower()]

print(f'=== GIT REPOSITORY AUDIT ===')
print(f'Total commits: {commits}')
print(f'Total merge commits: {len(merges)}')
print(f'Total Pull Requests (#): {len(prs)}')

languages = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.jsx': 'JavaScript',
    '.ts': 'TypeScript',
    '.tsx': 'TypeScript',
    '.sql': 'SQL'
}
loc_counts = {}
file_counts = {}
for root, dirs, files in os.walk('.'):
    norm_root = root.replace('\\', '/').lower()
    if any(p in norm_root for p in ['/.git', '/.venv', '/node_modules', '/__pycache__', '/tests', '/coverage', '/dist', '/build']):
        continue
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in languages:
            lang = languages[ext]
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                c = sum(1 for line in fp if line.strip())
            loc_counts[lang] = loc_counts.get(lang, 0) + c
            file_counts[lang] = file_counts.get(lang, 0) + 1

print('\n=== PRODUCTION CODE AUDIT (Excluding tests, venv, node_modules) ===')
for k, v in sorted(loc_counts.items(), key=lambda x: -x[1]):
    print(f'  {k}: {v:,} LOC across {file_counts.get(k, 0)} files')
print(f'Grand Total Prod LOC: {sum(loc_counts.values()):,}')
