import requests
import json
import os

PAGE_ID = "26299678719701649"
TOKEN = os.environ["FB_PAGE_TOKEN"]

url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/posts"
params = {
    "fields": "message,story,full_picture,created_time,permalink_url",
    "access_token": TOKEN,
    "limit": 20
}

response = requests.get(url, params=params)
data = response.json()

with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(data.get("data", []), f, ensure_ascii=False, indent=2)

print(f"已抓取 {len(data.get('data', []))} 篇貼文")
