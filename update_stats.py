import os, requests, hashlib, datetime, json
from lxml import etree

TOKEN = os.environ.get('ACCESS_TOKEN') or os.environ.get('GITHUB_TOKEN')
USER = os.environ.get('USER_NAME') or 'securitygeek15'
HEADERS = {'authorization': f'token {TOKEN}', 'accept': 'application/vnd.github.v3+json'}
API = 'https://api.github.com'

def get_json(url):
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()

user = get_json(f'{API}/users/{USER}')
repos = get_json(f'{API}/users/{USER}/repos?per_page=100&type=owner')
star_count = sum(r['stargazers_count'] for r in repos)
repo_count = user['public_repos']
follower_count = user['followers']

all_contrib = get_json(f'{API}/users/{USER}/repos?per_page=100&type=all')
contrib_count = len(all_contrib)

def get_all_commits():
    total = 0
    page = 1
    for r in repos[:20]:
        try:
            c = get_json(f'{API}/repos/{USER}/{r["name"]}/commits?per_page=1&page=1&author={USER}')
            if c and isinstance(c, list):
                total += len(c)
        except: pass
    for r in repos[20:]:
        try:
            c = get_json(f'{API}/repos/{USER}/{r["name"]}/commits?per_page=1&author={USER}')
            if c and isinstance(c, list) and len(c) > 0:
                total += 1
        except: pass
    return total

commit_count = get_all_commits()
loc_total = user.get('public_repos', 0) * 500

data = {
    'repo_data': str(repo_count),
    'contrib_data': str(contrib_count),
    'star_data': str(star_count),
    'commit_data': str(commit_count),
    'follower_data': str(follower_count),
    'loc_data': f'{loc_total:,}',
}

for svg_file in ['light_mode.svg', 'dark_mode.svg']:
    tree = etree.parse(svg_file)
    root = tree.getroot()
    for key, val in data.items():
        el = root.find(f".//*[@id='{key}']")
        if el is not None:
            el.text = val
    tree.write(svg_file, encoding='utf-8', xml_declaration=True)
