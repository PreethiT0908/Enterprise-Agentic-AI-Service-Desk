from database.db import SessionLocal
from models.ticket import Ticket


# =========================
# Save Ticket
# =========================

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

    return ticket



# =========================
# Get All Tickets
# =========================

def get_all_tickets():

    db = SessionLocal()

    tickets = (
        db.query(Ticket)
        .all()
    )

    db.close()

    return tickets



# =========================
# Update Ticket Status
# =========================

def update_ticket_status(ticket_id, new_status):

    db = SessionLocal()


    ticket = (
        db.query(Ticket)
        .filter(
            Ticket.ticket_id == ticket_id
        )
        .first()
    )


    if ticket:

        ticket.status = new_status

        db.commit()

        db.refresh(ticket)

        db.close()


        return {
            "message": "Ticket status updated successfully",
            "ticket_id": ticket.ticket_id,
            "status": ticket.status
        }


    db.close()


    return {
        "message": "Ticket not found"
    }