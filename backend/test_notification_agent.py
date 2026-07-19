from agents.notification_agent import send_notification

decision = {
    "resolved": False
}

ticket = {
    "ticket_id": "INC-1001"
}

routing = {
    "assigned_team": "Network Team"
}

result = send_notification(
    decision,
    ticket,
    routing
)

print("\n===== NOTIFICATION AGENT =====\n")
print(result)