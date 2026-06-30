from datetime import datetime
import json

def get_scholarships():
    # Today's date to check for expired opportunities automatically
    today = datetime.today().date()

    # Broad global dataset covering Degrees, Fellowships, and Exchange Programs
    all_scholarships = [
        # --- DEGREE PROGRAMS (Bachelor, Master, PhD) ---
        {
            "title": "Erasmus Mundus Joint Master Degrees (EMJMD)",
            "link": "https://www.eacea.ec.europa.eu/scholarships/emjmd-catalogue_en",
            "funding": "Fully Funded",
            "degree": "Master",
            "host_country": "Europe",
            "deadline": "2027-02-15"
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
            "title": "Fulbright Foreign Student Scholarship Program (USA)",
            "link": "https://foreign.fulbrightonline.org/",
            "funding": "Fully Funded",
            "degree": "Master, PhD",
            "host_country": "United States",
            "deadline": "2026-10-15"
        },
        {
            "title": "Stipendium Hungaricum Scholarship Program",
            "link": "https://stipendiumhungaricum.hu/",
            "funding": "Fully Funded",
            "degree": "Bachelor, Master, PhD",
            "host_country": "Hungary",
            "deadline": "2027-01-15"
        },
        {
            "title": "GKS - Global Korea Scholarship",
            "link": "https://www.studyinkorea.go.kr",
            "funding": "Fully Funded",
            "degree": "Bachelor, Master, PhD",
            "host_country": "South Korea",
            "deadline": "2027-03-10"
        },
        {
            "title": "MEXT Japan Undergraduate & Research Scholarships",
            "link": "https://www.pk.emb-japan.go.jp/itpr_en/MEXT_Scholarship.html",
            "funding": "Fully Funded",
            "degree": "Bachelor, Master, PhD",
            "host_country": "Japan",
            "deadline": "2027-05-15"
        },

        # --- FELLOWSHIPS (Professional & Research) ---
        {
            "title": "Hubert H. Humphrey Fellowship Program (USA)",
            "link": "https://www.humphreyfellowship.org/",
            "funding": "Fully Funded",
            "degree": "Fellowship",
            "host_country": "United States",
            "deadline": "2026-10-01"
        },
        {
            "title": "Lester B. Pearson International Fellowship (University of Toronto)",
            "link": "https://future.utoronto.ca/pearson/about/",
            "funding": "Fully Funded",
            "degree": "Fellowship",
            "host_country": "Canada",
            "deadline": "2027-01-15"
        },
        {
            "title": "CERN Senior Fellowship Programme",
            "link": "https://careers.cern/fellows",
            "funding": "Fully Funded",
            "degree": "Fellowship",
            "host_country": "Switzerland",
            "deadline": "2026-09-01"
        },
        {
            "title": "King Abdullah University (KAUST) Fellowship",
            "link": "https://www.kaust.edu.sa/en",
            "funding": "Fully Funded",
            "degree": "Master, PhD, Fellowship",
            "host_country": "Saudi Arabia",
            "deadline": "2027-01-05"
        },

        # --- EXCHANGE PROGRAMS (Short-Term & Cultural) ---
        {
            "title": "Global UGRAD Exchange Program (USA)",
            "link": "https://www.worldlearning.org/program/global-undergraduate-exchange-program/",
            "funding": "Fully Funded",
            "degree": "Exchange Program",
            "host_country": "United States",
            "deadline": "2026-12-15"
        },
        {
            "title": "SUSI Summer Exchange Program for Student Leaders",
            "link": "https://www.susi.org/",
            "funding": "Fully Funded",
            "degree": "Exchange Program",
            "host_country": "United States",
            "deadline": "2026-11-20"
        },
        {
            "title": "CrossCulture Programme (CCP) Exchange Germany",
            "link": "https://www.ifa.de/en/funding/crossculture-programme/",
            "funding": "Fully Funded",
            "degree": "Exchange Program",
            "host_country": "Germany",
            "deadline": "2026-12-31"
        },
        {
            "title": "YSEALI Academic Fellows Exchange Program",
            "link": "https://asean.usmission.gov/yseali/yseali-fellows/",
            "funding": "Fully Funded",
            "degree": "Exchange Program",
            "host_country": "Southeast Asia / USA",
            "deadline": "2026-10-25"
        }
    ]

    # Filter out expired listings automatically based on real-world timeline calendars
    active_scholarships = []
    for item in all_scholarships:
        try:
            deadline_date = datetime.strptime(item["deadline"], "%Y-%m-%d").date()
            if deadline_date >= today:
                active_scholarships.append(item)
        except ValueError:
            # Safe operational fallback mechanism
            active_scholarships.append(item)

    return {
        "total_scholarships": len(active_scholarships),
        "scholarships": active_scholarships
    }


def main():
    data = get_scholarships()

    with open("scholarships.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Master Database Compiled! Dynamic objects deployed: {data['total_scholarships']}")


if __name__ == "__main__":
    main()
