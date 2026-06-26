def get_scholarships():
    url = "https://www.scholarshipsads.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    scholarships = []

    # more flexible selectors
    for item in soup.find_all("a")[:15]:
        title = item.text.strip()
        link = item.get("href")

        if title and len(title) > 10 and link:
            if not link.startswith("http"):
                link = "https://www.scholarshipsads.com" + link

            scholarships.append({
                "title": title,
                "link": link
            })

    return scholarships
