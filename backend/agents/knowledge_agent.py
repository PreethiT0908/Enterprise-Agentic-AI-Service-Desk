# agents/knowledge_agent.py

knowledge_base = {

    "VPN": [
        "Verify internet connectivity",
        "Update VPN credentials",
        "Reconnect VPN profile",
        "Restart VPN client"
    ],

    "Printer": [
        "Check printer power",
        "Verify printer connection",
        "Restart print spooler",
        "Print a test page"
    ],

    "WiFi": [
        "Check if WiFi is enabled",
        "Restart the router",
        "Forget and reconnect the WiFi network",
        "Update network drivers"
    ],

    "Network": [
        "Check network cable connection",
        "Restart network adapter",
        "Verify IP configuration",
        "Check DNS settings"
    ],

    "Email": [
        "Verify internet connectivity",
        "Check email account configuration",
        "Re-enter email password",
        "Restart email application"
    ],

    "Outlook": [
        "Restart Outlook",
        "Repair Outlook profile",
        "Check mailbox connectivity",
        "Run Outlook in safe mode"
    ],

    "Password Reset": [
        "Verify user identity",
        "Reset account password",
        "Unlock account if locked",
        "Force password change on next login"
    ],

    "Software Installation": [
        "Verify administrator permissions",
        "Check software compatibility",
        "Download latest installer",
        "Restart system after installation"
    ]
}


def search_knowledge(category):

    solutions = knowledge_base.get(
        category,
        ["No solution found"]
    )

    return {
        "category": category,
        "solutions": solutions
    }