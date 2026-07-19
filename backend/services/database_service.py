from database import SessionLocal
from models.ticket import Ticket

def save_ticket(ticket_data):
    db = SessionLocal()

    ticket = Ticket(
        ticket_id=ticket_data["ticket_id"],
        category=ticket_data["category"],
        priority=ticket_data["priority"],
        status=ticket_data["status"],
        summary=ticket_data["summary"]
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    db.close()

    return {"message": "Ticket saved successfully"}