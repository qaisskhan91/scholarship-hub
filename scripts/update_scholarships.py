import json

def get_scholarships():
    # Clean structured scholarships (starter dataset)
    scholarships = [
        {
            "title": "Fulbright Scholarship Program",
            "link": "https://foreign.fulbrightonline.org/",
        },
        {
            "title": "DAAD Germany Scholarships",
            "link": "https://www.daad.de/en/",
        },
        {
            "title": "Erasmus Mundus Scholarships",
            "link": "https://www.eacea.ec.europa.eu/scholarships/emjmd-catalogue_en",
        },
        {
            "title": "Commonwealth Scholarships",
            "link": "https://cscuk.fcdo.gov.uk/apply/",
        },
        {
            "title": "HEC Pakistan Scholarships",
            "link": "https://www.hec.gov.pk/english/scholarshipsgrants/",
        }
    ]

    return {
        "total_scholarships": len(scholarships),
        "scholarships": scholarships
    }


def main():
    data = get_scholarships()

    with open("scholarships.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Clean scholarship database updated!")


if __name__ == "__main__":
    main()
