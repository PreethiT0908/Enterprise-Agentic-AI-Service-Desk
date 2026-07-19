import requests


BASE_URL = "http://127.0.0.1:8000"


# Get all tickets

def get_tickets_from_api():

    response = requests.get(
        f"{BASE_URL}/tickets/"
    )

    return response.json()



# Update ticket status

def update_ticket_status_api(ticket_id, status):

    response = requests.put(
        f"{BASE_URL}/tickets/{ticket_id}/status",
        params={
            "status": status
        }
    )

    return response.json()