# quotes.py
import requests
from html import unescape
from datetime import datetime

url = "https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand&per_page=1"

try:
    res = requests.get(url, headers={"Accept": "application/json"})
    res.raise_for_status()
    data = res.json()[0]

    quote = unescape(data['content']['rendered']).strip().replace("<p>", "").replace("</p>", "")
    author = data['title']['rendered'].strip()
    today = datetime.now().strftime("%Y-%m-%d")

    readme_content = f"""\
# 📘 Daily Design Quote

> 💬 **"{quote}"**  
> — *{author}*  
> 📅 *{today}*

---

> 이 명언은 매일 [Quotes on Design](https://quotesondesign.com) API로 자동 업데이트됩니다.
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

except Exception as e:
    print(f"Error: {e}")
