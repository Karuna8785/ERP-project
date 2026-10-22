import os

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

print('Current prod LOC on disk (excluding tests, venv, node_modules):')
for k, v in loc_counts.items():
    print(f'  {k}: {v} LOC across {file_counts.get(k, 0)} files')
print('Total prod LOC:', sum(loc_counts.values()))
