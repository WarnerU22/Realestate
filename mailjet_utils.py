from mailjet_rest import Client


def send_leads_via_mailjet(leads, config):
    required = [
        "mailjet_api_key",
        "mailjet_api_secret",
        "mailjet_sender",
        "mailjet_recipient",
    ]
    if not all(config.get(k) for k in required):
        print("[-] Mailjet configuration incomplete, skipping email.")
        return

    if not leads:
        print("[-] No leads to email.")
        return

    mailjet = Client(auth=(config["mailjet_api_key"], config["mailjet_api_secret"]), version="v3.1")
    body = "\n".join(
        f"${lead['price']:,.0f} {lead['address']} ({lead['link']})" for lead in leads
    )

    data = {
        "Messages": [
            {
                "From": {"Email": config["mailjet_sender"], "Name": "Leadbot"},
                "To": [{"Email": config["mailjet_recipient"]}],
                "Subject": "New Real Estate Leads",
                "TextPart": body,
            }
        ]
    }

    try:
        result = mailjet.send.create(data=data)
        print(f"[+] Sent email via Mailjet with status {result.status_code}")
    except Exception as e:
        print(f"[-] Failed to send email via Mailjet: {e}")
