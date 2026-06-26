def get_scholarships():
    url = "https://www.scholarshipsads.com/category/scholarships/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers, timeout=20)
    soup = BeautifulSoup(response.text, "html.parser")

    scholarships = []

    # TRY multiple possible structures
    selectors = [
        "h2 a",
        "h2.entry-title a",
        "article h2 a",
        ".entry-title a"
    ]

    seen = set()

    for selector in selectors:
        posts = soup.select(selector)

        for post in posts:
            title = post.text.strip()
            link = post.get("href")

            if not title or not link:
                continue

            if len(title) < 10:
                continue

            if link in seen:
                continue

            seen.add(link)

            if not link.startswith("http"):
                link = "https://www.scholarshipsads.com" + link

            scholarships.append({
                "title": title,
                "link": link
            })

    return scholarships[:10]
