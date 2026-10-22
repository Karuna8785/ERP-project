import requests
import json

url = 'https://train-plex-checker-bot-1--ttejaswar1234.replit.app/api/check'
print('Uploading SmartERP_Enterprise_v1.1.0.zip to test checker...')
with open('SmartERP_Enterprise_v1.1.0.zip', 'rb') as f:
    files = {'file': ('SmartERP_Enterprise_v1.1.0.zip', f, 'application/zip')}
    res = requests.post(url, files=files, timeout=120)

if res.status_code == 200:
    data = res.json()
    with open('checker_response.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print('Saved full response to checker_response.json')
    summary = data.get('trainplex', {}).get('summary', {})
    print('Overall:', summary.get('overall'))
    print('Score:', summary.get('score'))
    print('LOC:', summary.get('loc'))
    print('By lang:', summary.get('by_lang'))
    print('Git:', summary.get('git'))
    print('\nTrainPlex Checks:')
    for c in data.get('trainplex', {}).get('checks', []):
        status = c.get('status')
        name = c.get('name')
        val = c.get('value')
        req = c.get('required')
        print(f"  [{status.upper()}] {name} -> value: {val} (req: {req})")
else:
    print('Error:', res.status_code, res.text[:2000])
