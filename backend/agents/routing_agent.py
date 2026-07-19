def route_ticket(category):

    team_mapping = {

        "VPN": "Network Team",

        "Password": "Identity Team",

        "Email": "Messaging Team",

        "Printer": "Desktop Support Team",

        "Database": "DBA Team",

        "Cloud": "Cloud Operations Team",

        "Security": "SOC Team"
    }

    assigned_team = team_mapping.get(
        category,
        "General Support Team"
    )

    return {
        "category": category,
        "assigned_team": assigned_team
    }