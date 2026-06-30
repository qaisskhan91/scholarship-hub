from datetime import datetime
import json

def get_scholarships():
    # Today's date to check for expired opportunities automatically
    today = datetime.today().date()

    # Upgraded structured dataset matching the new filter matrix
    all_scholarships = [
        {
            "title": "Fulbright Scholarship Program 2027 (USA)",
            "link": "https://foreign.fulbrightonline.org/",
            "funding": "Fully Funded",
            "degree": "Master, PhD",
            "host_country": "United States",
            "deadline": "2026-10-15"
        },
        {
            "title": "DAAD Postgraduate Germany Scholarships",
            "link": "https://www.daad.de/en/",
            "funding": "Fully Funded",
            "degree": "Master, PhD",
            "host_country": "Germany",
            "deadline": "2026-10-31"
        },
        {
            "title": "Erasmus Mundus Joint Master Degrees (EMJMD)",
            "link": "https://www.eacea.ec.europa.eu/scholarships/emjmd-catalogue_en",
            "funding": "Fully Funded",
            "degree": "Master",
            "host_country": "Europe",
            "deadline": "2027-02-15"
        },
        {
            "title": "Commonwealth Scholarships for Developing Countries",
            "link": "https://cscuk.fcdo.gov.uk/apply/",
            "funding": "Fully Funded",
            "degree": "Master, PhD",
            "host_country": "United Kingdom",
            "deadline": "2026-12-10"
        },
        {
            "title": "HEC Pakistan Overseas Scholarship Phase-III",
            "link": "https://www.hec.gov.pk/english/scholarshipsgrants/",
            "funding": "Fully Funded",
            "degree": "PhD",
            "host_country": "Global",
            "deadline": "2026-09-30"
        },
        {
            "title": "MEXT Japan Research Student Scholarship",
            "link": "https://www.pk.emb-japan.go.jp/itpr_en/MEXT_Scholarship.html",
            "funding": "Fully Funded",
            "degree": "Master, PhD",
            "host_country": "Japan",
            "deadline": "2027-05-15"
        }
    ]

    # Filter out expired scholarships dynamically
    active_scholarships = []
    for item in all_scholarships:
        try:
            # Parse the YYYY-MM-DD string into a clean date object
            deadline_date = datetime.strptime(item["deadline"], "%Y-%m-%d").date()
            if deadline_date >= today:
                active_scholarships.append(item)
        except ValueError:
            # Fallback check in case formatting fails
            active_scholarships.append(item)

    return {
        "total_scholarships": len(active_scholarships),
        "scholarships": active_scholarships
    }


def main():
    data = get_scholarships()

    # Writes clean outputs formatted explicitly to align with the frontend portal mapping engine
    with open("scholarships.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Clean database generated successfully! Active entries tracked: {data['total_scholarships']}")


if __name__ == "__main__":
    main()
