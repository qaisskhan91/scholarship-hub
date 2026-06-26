import feedparser
import json

def get_scholarships():
    url = "https://news.google.com/rss/search?q=scholarships+pakistan"

    feed = feedparser.parse(url)

    scholarships = []

    for entry in feed.entries[:10]:
        scholarships.append({
            "title": entry.title,
            "link": entry.link
        })

    return scholarships


def main():
    data = get_scholarships()

    output = {
        "total_scholarships": len(data),
        "scholarships": data
    }

    with open("scholarships.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print("Updated real scholarships successfully!")


if __name__ == "__main__":
    main()
