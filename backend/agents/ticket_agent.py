import random


def create_ticket(category, priority, summary):

    ticket_id = f"INC-{random.randint(1000,9999)}"

    return {
        "ticket_id": ticket_id,
        "status": "OPEN",
        "category": category,
        "priority": priority,
        "summary": summary
    }