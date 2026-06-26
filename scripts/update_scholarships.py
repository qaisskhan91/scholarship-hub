import requests
from bs4 import BeautifulSoup
import json

def get_scholarships():
    url = "https://www.scholarshipsads.com/category/scholarships/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    scholarships = []

    posts = soup.select("h2.entry-title a")

    for post in posts[:10]:
        title = post.text.strip()
        link = post.get("href")

        if title and link:
            scholarships.append({
                "title": title,
                "link": link
            })

    return scholarships


def main():
    data = get_scholarships()

    output = {
        "total_scholarships": len(data),
        "scholarships": data
    }

    with open("scholarships.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print("Real scholarships updated successfully!")


if __name__ == "__main__":
    main()
