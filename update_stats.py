import os
import json
import urllib.request
import xml.etree.ElementTree as ET

# Configuration
TOKEN = os.environ.get('GITHUB_TOKEN')
USER = os.environ.get('USER_NAME', 'securitygeek15')
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'Python-urllib'
}
if TOKEN:
    HEADERS['Authorization'] = f'token {TOKEN}'

API_URL = 'https://api.github.com'

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    print(f"Fetching stats for {USER}...")
    
    user_data = fetch_json(f'{API_URL}/users/{USER}') or {}
    followers = user_data.get('followers', 0)
    public_repos = user_data.get('public_repos', 0)
    
    repos = fetch_json(f'{API_URL}/users/{USER}/repos?per_page=100&type=owner') or []
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    
    # search API requires special accept header
    search_req = urllib.request.Request(f'{API_URL}/search/commits?q=author:{USER}', headers={
        **HEADERS, 'Accept': 'application/vnd.github.cloak-preview'
    })
    total_commits = 0
    try:
        with urllib.request.urlopen(search_req) as response:
            search_data = json.loads(response.read().decode())
            total_commits = search_data.get('total_count', 0)
    except Exception as e:
        print(f"Error fetching commits: {e}")

    all_repos = fetch_json(f'{API_URL}/users/{USER}/repos?per_page=100&type=all') or []
    contributed = len(all_repos)
    
    stats = {
        'repo_data': str(public_repos),
        'contrib_data': str(contributed),
        'star_data': str(total_stars),
        'commit_data': str(total_commits),
        'follower_data': str(followers)
    }
    
    print(f"Stats fetched: {stats}")
    
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    
    for svg_file in ['dark_mode.svg', 'light_mode.svg']:
        if not os.path.exists(svg_file):
            print(f"File {svg_file} not found. Skipping.")
            continue
            
        tree = ET.parse(svg_file)
        root = tree.getroot()
        
        for key, val in stats.items():
            for elem in root.iter():
                if elem.attrib.get('id') == key:
                    elem.text = str(val)
                    
        tree.write(svg_file, encoding='utf-8', xml_declaration=True)
        print(f"Updated {svg_file}")

if __name__ == '__main__':
    main()
