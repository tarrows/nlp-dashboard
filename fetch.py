import json
import requests

data = './data'
url = 'https://hacker-news.firebaseio.com/v0'


def fetch_hn(save_dir: str, base_url: str, take=50):
    stories = requests.get(f'{base_url}/topstories.json').json()
    for story_id in stories[:take]:
        story = requests.get(f'{base_url}/item/{story_id}.json').json()
        try:
            with open(f'{save_dir}/{story_id}.json', mode='x', encoding='utf-8') as f:
                json.dump(story, f, indent=2)
        except FileExistsError:
            pass


if __name__ == '__main__':
    fetch_hn(data, url)
