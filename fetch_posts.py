import requests
import json
import os

TOKEN = os.environ["FB_PAGE_TOKEN"]

# 先查這個 Token 能存取哪些粉專
url = "https://graph.facebook.com/v19.0/me/accounts"
params = {"access_token": TOKEN}

response = requests.get(url, params=params)
data = response.json()

print("可存取的粉專：", json.dumps(data, ensure_ascii=False, indent=2))

# 如果有找到粉專，用第一個的 token 抓貼文
pages = data.get("data", [])
if pages:
    page = pages[0]
    print(f"\n使用粉專：{page.get('name')} (ID: {page.get('id')})")
    page_token = page.get("access_token")
    
    posts_url = f"https://graph.facebook.com/v19.0/{page['id']}/posts"
    posts_params = {
        "fields": "message,story,full_picture,created_time,permalink_url",
        "access_token": page_token,
        "limit": 20
    }
    posts_response = requests.get(posts_url, params=posts_params)
    posts_data = posts_response.json()
    print("\n貼文結果：", json.dumps(posts_data, ensure_ascii=False, indent=2))
    
    with open("posts.json", "w", encoding="utf-8") as f:
        json.dump(posts_data.get("data", []), f, ensure_ascii=False, indent=2)
    print(f"\n已抓取 {len(posts_data.get('data', []))} 篇貼文")
else:
    print("找不到可存取的粉專，請確認 Token 權限")
    with open("posts.json", "w") as f:
        json.dump([], f)
