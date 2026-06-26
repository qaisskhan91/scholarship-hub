import requests
from bs4 import BeautifulSoup
import json

def get_scholarships():
    url = "https://www.scholarshipsads.com/"  # sample public site

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    scholarships = []

    # extract titles (simple generic method)
    for item in soup.select("h2 a")[:10]:
        title = item.text.strip()
        link = item.get("href")

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

    with open("scholarships.json", "w") as f:
        json.dump(output, f, indent=4)

    print("Real scholarships updated!")

if __name__ == "__main__":
    main()
