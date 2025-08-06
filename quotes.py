import requests
from html import unescape
from datetime import datetime, timezone, timedelta

URL = "https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand&per_page=1"
README_PATH = "README.md"

def get_quote():
    """Quotes on Design에서 랜덤 명언을 가져옴. 데이터가 없으면 다시 요청."""
    for _ in range(5):  # 최대 5번까지 재시도
        response = requests.get(URL, headers={"Accept": "application/json"})
        if response.status_code == 200:
            data = response.json()
            if data:
                quote = unescape(data[0]['content']['rendered']).strip().replace("<p>", "").replace("</p>", "")
                author = data[0]['title']['rendered'].strip()
                if quote:
                    return quote, author
    # 여기까지 도달하면 실패
    return "항상 노력하라. 운은 준비된 자에게 온다.", "Seneca"

def update_readme():
    quote, author = get_quote()
    now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S")  # 한국 시간

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
