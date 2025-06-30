import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0"}

def generate_urls(regions):
    """Generate Zillow FSBO URLs for a list of region codes."""
    return [f"https://www.zillow.com/homes/fsbo/{code}_rb/" for code in regions]

def parse_price(text):
    text = (
        text.replace("$", "")
        .replace(",", "")
        .split()[0]
    )
    try:
        return int(text)
    except ValueError:
        return None


def scrape_zillow(url):
    """Scrape a single Zillow FSBO page."""
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    listings = soup.select("article")
    results = []
    for listing in listings:
        link = listing.find("a", href=True)
        price = listing.find("span", {"data-test": "property-card-price"})
        address = listing.find("address")
        if link and price and address:
            results.append(
                {
                    "link": "https://www.zillow.com" + link["href"],
                    "price": parse_price(price.get_text(strip=True)),
                    "address": address.get_text(strip=True),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
    return results


def filter_under_market(leads, discount):
    """Return listings priced below the average by a given discount."""
    prices = [lead["price"] for lead in leads if isinstance(lead.get("price"), int)]
    if not prices:
        return []
    avg_price = sum(prices) / len(prices)
    threshold = avg_price * (1 - discount)
    return [lead for lead in leads if isinstance(lead.get("price"), int) and lead["price"] <= threshold]
