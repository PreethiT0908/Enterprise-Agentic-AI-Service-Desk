from agents.incident_agent import analyze_incident
from agents.knowledge_agent import search_knowledge
from agents.troubleshooting_agent import get_troubleshooting_steps
from agents.automation_agent import automate_resolution
from agents.decision_agent import make_decision
from agents.ticket_agent import create_ticket
from agents.routing_agent import route_ticket
from agents.notification_agent import send_notification

from services.ticket_service import save_ticket



def run_workflow(incident_text):

    # -----------------------------
    # Incident Analysis Agent
    # -----------------------------

    incident = analyze_incident(
        incident_text
    )

    print("\nINCIDENT ANALYSIS")
    print(incident)



    # -----------------------------
    # Knowledge Agent
    # -----------------------------

    knowledge = search_knowledge(
        incident["category"]
    )

    print("\nKNOWLEDGE BASE")
    print(knowledge)



    # -----------------------------
    # Troubleshooting Agent
    # -----------------------------

    troubleshooting = get_troubleshooting_steps(
        incident["category"]
    )

    print("\nTROUBLESHOOTING")
    print(troubleshooting)



    # -----------------------------
    # Automation Agent
    # -----------------------------

    automation = automate_resolution(
        incident["category"]
    )

    print("\nAUTOMATION")
    print(automation)



    # -----------------------------
    # Decision Agent
    # -----------------------------

    decision = make_decision(
        automation
    )

    print("\nDECISION")
    print(decision)



    # =============================
    # CASE 1: Automatically Resolved
    # =============================

    if decision["resolved"]:

        return {

            "incident": incident,

            "knowledge": knowledge,

            "troubleshooting": troubleshooting,

            "automation": automation,

            "decision": decision,

            "message": "Issue resolved automatically"

        }



    # =============================
    # CASE 2: Create Ticket
    # =============================

    else:


        ticket = create_ticket(

            incident["category"],

            incident["urgency"],

            incident["summary"]

        )


        print("\nTICKET")
        print(ticket)



        # Save to PostgreSQL

        save_ticket(ticket)


        print(
            "\nTICKET SAVED TO DATABASE"
        )



        # Routing Agent

        routing = route_ticket(

            ticket["category"]

        )


        print("\nROUTING")
        print(routing)



        # Notification Agent

        notification = send_notification(

            ticket["ticket_id"],

            routing["assigned_team"]

        )


        print("\nNOTIFICATION")
        print(notification)



        return {


            "incident": incident,


            "knowledge": knowledge,


            "troubleshooting": troubleshooting,


            "automation": automation,


            "decision": decision,


            "ticket": ticket,


            "routing": routing,


            "notification": notification,


            "message": "Ticket created successfully"

        }