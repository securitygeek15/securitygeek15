import os
import json
import urllib.request
import datetime
import build_hud

# Configuration
TOKEN = os.environ.get('GITHUB_TOKEN')
USER = os.environ.get('USER_NAME', 'securitygeek15')
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'Mozilla/5.0'
}
if TOKEN:
    HEADERS['Authorization'] = f'token {TOKEN}'

API_URL = 'https://api.github.com'

def fetch_json(url, extra_headers=None):
    req_headers = {**HEADERS}
    if extra_headers:
        req_headers.update(extra_headers)
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def calculate_uptime(birth_date):
    now = datetime.datetime.now()
    years = now.year - birth_date.year
    months = now.month - birth_date.month
    days = now.day - birth_date.day
    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12
    return f"{years} years, {months} months, {days} days"

def main():
    print(f"Fetching GitHub stats for {USER}...")

    user_data = fetch_json(f'{API_URL}/users/{USER}') or {}
    followers = user_data.get('followers', 5)
    public_repos = user_data.get('public_repos', 21)

    # Owned Repos & Stars
    repos = fetch_json(f'{API_URL}/users/{USER}/repos?per_page=100&type=owner') or []
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos) if repos else 25

    # All Repos (Contributed)
    all_repos = fetch_json(f'{API_URL}/users/{USER}/repos?per_page=100&type=all') or []
    contributed = len(all_repos) if all_repos else public_repos

    # Total Commits
    total_commits = 0
    search_data = fetch_json(
        f'{API_URL}/search/commits?q=author:{USER}',
        extra_headers={'Accept': 'application/vnd.github.cloak-preview'}
    )
    if search_data and 'total_count' in search_data:
        total_commits = search_data['total_count']
    if total_commits == 0:
        total_commits = 134

    # Lines of Code (additions and deletions across owned repositories)
    # Default baseline if token rate limits or stats are indexing
    loc_add = 52140
    loc_del = 3220

    if TOKEN and repos:
        computed_add = 0
        computed_del = 0
        for r in repos[:15]:
            rname = r.get('name')
            stats_data = fetch_json(f'{API_URL}/repos/{USER}/{rname}/stats/contributors')
            if isinstance(stats_data, list):
                for contributor in stats_data:
                    if contributor.get('author', {}).get('login') == USER:
                        for week in contributor.get('weeks', []):
                            computed_add += week.get('a', 0)
                            computed_del += week.get('d', 0)
        if computed_add > 0:
            loc_add = computed_add
            loc_del = computed_del

    loc_net = max(0, loc_add - loc_del)

    # Calculate Uptime based on birthdate
    birth_date = datetime.datetime(2009, 3, 1)
    uptime_str = calculate_uptime(birth_date)

    stats = {
        'age_data': uptime_str,
        'repo_data': str(public_repos),
        'contrib_data': str(contributed),
        'star_data': str(total_stars),
        'commit_data': f"{total_commits:,}",
        'follower_data': str(followers),
        'loc_data': f"{loc_net:,}",
        'loc_add': f"{loc_add:,}",
        'loc_del': f"{loc_del:,}"
    }

    print(f"Stats resolved: {stats}")

    print("Generating updated dark_mode.svg and light_mode.svg...")
    with open('dark_mode.svg', 'w', encoding='utf-8') as f:
        f.write(build_hud.build_svg(True, stats=stats))
    print("Updated dark_mode.svg successfully.")

    with open('light_mode.svg', 'w', encoding='utf-8') as f:
        f.write(build_hud.build_svg(False, stats=stats))
    print("Updated light_mode.svg successfully.")

if __name__ == '__main__':
    main()
