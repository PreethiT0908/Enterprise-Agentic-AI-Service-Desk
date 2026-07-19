from agents.incident_agent import analyze_incident
from agents.knowledge_agent import search_knowledge
from agents.troubleshooting_agent import get_troubleshooting_steps
from agents.automation_agent import automate_resolution
from agents.decision_agent import make_decision
from agents.ticket_agent import create_ticket
from agents.routing_agent import route_ticket
from agents.notification_agent import send_notification

from services.ticket_service import save_ticket


def run_workflow():

    # Change this line to test different incidents
    incident_text = "Office printer is offline and not printing documents"

    # Incident Analysis
    incident = analyze_incident(incident_text)

    print("\nINCIDENT ANALYSIS")
    print(incident)

    # Knowledge Base
    knowledge = search_knowledge(
        incident["category"]
    )

    print("\nKNOWLEDGE BASE")
    print(knowledge)

    # Troubleshooting
    troubleshooting = get_troubleshooting_steps(
        incident["category"]
    )

    print("\nTROUBLESHOOTING")
    print(troubleshooting)

    # Automation
    automation = automate_resolution(
        incident["category"]
    )

    print("\nAUTOMATION")
    print(automation)

    # Decision
    decision = make_decision(
        automation
    )

    print("\nDECISION")
    print(decision)

    if not decision["resolved"]:

        # Create Ticket
        ticket = create_ticket(
            incident["category"],
            incident["urgency"],
            incident["summary"]
        )

        print("\nTICKET")
        print(ticket)

        # Save Ticket
        save_ticket(ticket)

        print("\nTICKET SAVED TO DATABASE")

        # Route Ticket
        routing = route_ticket(
            ticket["category"]
        )

        print("\nROUTING")
        print(routing)

        # Notification
        notification = send_notification(
            ticket["ticket_id"],
            routing["assigned_team"]
        )

        print("\nNOTIFICATION")
        print(notification)

    else:

        print("\nISSUE RESOLVED AUTOMATICALLY")


if __name__ == "__main__":
    run_workflow()