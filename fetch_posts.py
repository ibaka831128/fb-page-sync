import requests
import json
import os

TOKEN = os.environ["FB_PAGE_TOKEN"]

# Page Access Token 下，/me 就是粉專本身
url = "https://graph.facebook.com/v19.0/me/posts"
params = {
    "fields": "message,story,full_picture,created_time,permalink_url",
    "access_token": TOKEN,
    "limit": 20
}

response = requests.get(url, params=params)
data = response.json()

print("API 回應：", json.dumps(data, ensure_ascii=False, indent=2))

with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(data.get("data", []), f, ensure_ascii=False, indent=2)

print(f"已抓取 {len(data.get('data', []))} 篇貼文")
