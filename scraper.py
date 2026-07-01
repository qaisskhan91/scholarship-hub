import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_hec_scholarships():
    """Scrapes latest global/local opportunities listed on HEC portal."""
    url = "https://www.hec.gov.pk/site/scholarships"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    scholarships_list = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the main scholarship tables or link lists
            # Note: HEC uses standard list items/anchors for active items
            links = soup.find_all('a', href=True)
            
            for link in links:
                text = link.text.strip()
                href = link['href']
                
                # Filter for links that are actually scholarship announcements
                if "Scholarship" in text or "Fellowship" in text:
                    # Resolve relative URLs
                    full_url = href if href.startswith('http') else f"https://www.hec.gov.pk{href}"
                    
                    # Auto-assign levels based on title keywords
                    level = "Master/PhD"
                    if "Undergraduate" in text or "Bachelors" in text:
                        level = "Bachelor"
                    elif "Post Doctoral" in text or "Fellowship" in text:
                        level = "Fellowship"

                    # Format extracted info
                    scholarships_list.append({
                        "title": text,
                        "degree_level": level,
                        "category": "Fellowship" if "Fellowship" in text else "Scholarship",
                        "coverage": "Fully Funded",
                        "deadline": str(datetime.now().date()), # Temporary placeholder date
                        "link": full_url
                    })
    except Exception as e:
        print(f"Error scraping live HEC data: {e}")
        
    return scholarships_list


def get_global_fallbacks():
    """Returns updated standard global programs as dynamic fallbacks."""
    return [
        {
            "title": "Stipendium Hungaricum Scholarship Programme",
            "degree_level": "Bachelor/Master/PhD",
            "category": "Scholarship",
            "coverage": "Fully Funded",
            "deadline": "2027-01-15",
            "link": "https://stipendiumhungaricum.hu/"
        },
        {
            "title": "DAAD Development-Related Postgraduate Courses (EPOS)",
            "degree_level": "Master/PhD",
            "category": "Scholarship",
            "coverage": "Fully Funded",
            "deadline": "2026-10-31",
            "link": "https://www.daad.de/en/studying-in-germany/scholarships/"
        },
        {
            "title": "Global UGRAD Exchange Program",
            "degree_level": "Bachelor",
            "category": "Exchange Program",
            "coverage": "Fully Funded",
            "deadline": "2026-12-15",
            "link": "https://www.worldlearning.org/program/global-undergraduate-exchange-program/"
        }
    ]


if __name__ == "__main__":
    print("Starting automated scholarship aggregation...")
    
    # Gather items from scripts
    live_items = scrape_hec_scholarships()
    fallback_items = get_global_fallbacks()
    
    # Combine lists and eliminate any duplicates based on link
    all_scholarships = live_items + fallback_items
    unique_scholarships = {item['link']: item for item in all_scholarships}.values()
    
    # Rewrite the local data file
    with open('scholarships.json', 'w', encoding='utf-8') as f:
        json.dump(list(unique_scholarships), f, indent=4, ensure_ascii=False)
        
    print(f"Successfully sync'd {len(unique_scholarships)} entries into scholarships.json!")
