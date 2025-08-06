# quotes.py
import requests
from html import unescape

url = "https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand&per_page=1"

try:
    response = requests.get(url, headers={"Accept": "application/json"})
    response.raise_for_status()

    data = response.json()[0]
    quote = unescape(data['content']['rendered']).strip().replace("<p>", "").replace("</p>", "")
    author = data['title']['rendered'].strip()

    print(f"💬 \"{quote}\"\n— {author}")

except Exception as e:
    print(f"Failed to fetch quote: {e}")
