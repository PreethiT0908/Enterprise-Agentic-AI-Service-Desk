def send_notification(ticket_id, team):

    return {
        "notification_type": "TICKET_CREATED",
        "message": f"Ticket {ticket_id} created and assigned to {team}."
    }