from agents.incident_agent import analyze_incident
from agents.knowledge_agent import search_knowledge
from agents.troubleshooting_agent import get_troubleshooting_steps
from agents.automation_agent import execute_automation
from agents.decision_agent import make_decision
from agents.ticket_agent import create_ticket
from agents.routing_agent import route_ticket
from agents.notification_agent import send_notification


def process_incident(user_issue: str):

    # Agent 1 - Incident Agent
    incident = analyze_incident(user_issue)

    # Agent 2 - Knowledge Agent
    knowledge = search_knowledge(
        incident["category"]
    )

    # Agent 3 - Troubleshooting Agent
    troubleshooting = get_troubleshooting_steps(
        incident["category"]
    )

    # Agent 4 - Automation Agent
    automation = execute_automation(
        incident["category"]
    )

    # Agent 5 - Decision Agent
    decision = make_decision(
        automation
    )

    # Base response
    result = {
        "incident": incident,
        "knowledge": knowledge,
        "troubleshooting": troubleshooting,
        "automation": automation,
        "decision": decision
    }

    # Agent 6, 7, 8
    if not decision["resolved"]:

        # Agent 6 - Ticket Agent
        ticket = create_ticket(incident)

        # Agent 7 - Routing Agent
        routing = route_ticket(
            incident["category"]
        )

        # Agent 8 - Notification Agent
        notification = send_notification(
            decision,
            ticket,
            routing
        )

        result["ticket"] = ticket
        result["routing"] = routing
        result["notification"] = notification

    else:

        # Agent 8 - Notification Agent
        notification = send_notification(
            decision
        )

        result["notification"] = notification

    return result