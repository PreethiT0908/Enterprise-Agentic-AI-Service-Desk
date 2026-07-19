from fastapi import APIRouter, HTTPException
from services.ticket_service import (
    get_all_tickets,
    update_ticket_status,
    save_ticket
)

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


# =========================
# GET ALL TICKETS
# =========================

@router.get("/")
def get_tickets():

    tickets = get_all_tickets()

    return [
        {
            "ticket_id": ticket.ticket_id,
            "category": ticket.category,
            "priority": ticket.priority,
            "status": ticket.status,
            "summary": ticket.summary
        }
        for ticket in tickets
    ]



# =========================
# GET SINGLE TICKET
# =========================

@router.get("/{ticket_id}")
def get_ticket(ticket_id:str):

    tickets = get_all_tickets()

    for ticket in tickets:

        if ticket.ticket_id == ticket_id:

            return {
                "ticket_id": ticket.ticket_id,
                "category": ticket.category,
                "priority": ticket.priority,
                "status": ticket.status,
                "summary": ticket.summary
            }


    raise HTTPException(
        status_code=404,
        detail="Ticket not found"
    )



# =========================
# UPDATE STATUS
# =========================

@router.put("/{ticket_id}/status")
def change_status(
    ticket_id:str,
    status:str
):

    result = update_ticket_status(
        ticket_id,
        status
    )

    return result