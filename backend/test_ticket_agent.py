from agents.ticket_agent import create_ticket

incident = {
    "category": "VPN",
    "urgency": "Medium",
    "summary": "VPN connection failed after password reset."
}

ticket = create_ticket(incident)

print("\n===== TICKET AGENT =====\n")
print(ticket)