import csv

from config import load_config
from zillow_scraper import generate_urls, scrape_zillow, filter_under_market


def main():
    config = load_config()
    print(f"[+] Scraping Zillow for regions: {config['regions']}")

    leads = []
    for url in generate_urls(config['regions']):
        leads.extend(scrape_zillow(url))

    print(f"[+] Scraped {len(leads)} total listings.")

    filtered = filter_under_market(leads, config['discount_threshold'])
    print(
        f"[+] {len(filtered)} listings under market by {config['discount_threshold']*100}%"
    )

    with open(config['output_csv'], 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['price', 'address', 'link', 'timestamp'])
        writer.writeheader()
        writer.writerows(filtered)

    print(f"[+] Saved leads to {config['output_csv']}")


    # Display the first few leads for convenience
    print("[+] Top scraped leads:")
    for lead in filtered[:10]:
        print(
            f" - ${lead['price']:,.0f} {lead['address']} (" f"{lead['link']})"
        )


if __name__ == "__main__":
    main()
