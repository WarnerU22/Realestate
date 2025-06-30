import csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

    html_content = "<h3>Zillow FSBO Leads</h3><ul>"
    for lead in filtered[:10]:
        html_content += (
            f"<li><strong>${lead['price']:,.0f}</strong> – {lead['address']}<br>"
            f"<a href='{lead['link']}'>View Listing</a><br>"
            f"<small>{lead['timestamp']}</small></li><br>"
        )
    html_content += "</ul>"

    print("[+] Sending email via SendGrid API...")

    message = Mail(
        from_email=config['from_email'],
        to_emails=config['to_email'],
        subject='Real Estate Leads',
        html_content=html_content,
    )

    try:
        sg = SendGridAPIClient(config['sendgrid_api_key'])
        response = sg.send(message)
        print("✅ Email sent! Status code:", response.status_code)
    except Exception as e:
        print("❌ Failed to send email:", e)


if __name__ == "__main__":
    main()
