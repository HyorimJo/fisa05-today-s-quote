# quotes.py
# pip install requests
import requests
from html import unescape
from datetime import datetime, timezone, timedelta

URL = "https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand&per_page=1"
README_PATH = "README.md"

def get_quote():
    """Quotes on Design에서 랜덤 명언을 가져옴"""
    response = requests.get(URL, headers={"Accept": "application/json"})
    if response.status_code == 200:
        data = response.json()[0]
        quote = unescape(data['content']['rendered']).strip().replace("<p>", "").replace("</p>", "")
        author = data['title']['rendered'].strip()
        return quote, author
    else:
        return "명언을 불러올 수 없습니다.", "Unknown"

def update_readme():
    """README.md 파일 생성 또는 덮어쓰기"""
    quote, author = get_quote()
    now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S")  # KST 기준 시간

    readme_content = f"""
# 📘 Daily Design Quote

> 💬 **"{quote}"**  
> — *{author}*

⏳ 업데이트 시간: {now} (KST)

---

자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()
