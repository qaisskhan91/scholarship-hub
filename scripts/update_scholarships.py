import feedparser
import json
import re

def get_scholarships():
    # Google News RSS focused on scholarships
    url = "https://news.google.com/rss/search?q=scholarship+apply+2026+pakistan"

    feed = feedparser.parse(url)

    scholarships = []

    # keywords to keep only useful results
    keywords = [
        "scholarship",
        "apply",
        "funded",
        "fully funded",
        "fellowship",
        "grant",
        "financial aid",
        "program",
        "opportunity"
    ]

    for entry in feed.entries:
        title = entry.title.lower()

        # filter only relevant scholarship content
        if any(word in title for word in keywords):
            clean_title = re.sub(r'\s+', ' ', entry.title).strip()

            scholarships.append({
                "title": clean_title,
                "link": entry.link
            })

        # limit results
        if len(scholarships) >= 10:
            break

    output = {
        "total_scholarships": len(scholarships),
        "scholarships": scholarships
    }

    return output


def main():
    data = get_scholarships()

    with open("scholarships.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Clean scholarship data updated successfully!")


if __name__ == "__main__":
    main()
