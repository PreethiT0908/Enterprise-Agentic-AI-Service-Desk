def get_troubleshooting_steps(category):

    troubleshooting_db = {
        "VPN": [
            "Can you access the internet?",
            "Have you updated your VPN credentials?",
            "Are you using the latest VPN client version?",
            "Please restart the VPN client and try again."
        ],

        "Password": [
            "Did you recently change your password?",
            "Is your account locked?",
            "Please reset your password and try again."
        ],

        "Email": [
            "Can you send emails?",
            "Can you receive emails?",
            "Please restart Outlook and try again."
        ],

        "Printer": [
            "Is the printer powered on?",
            "Check printer cable or network connection.",
            "Restart the printer.",
            "Try printing a test page."
        ],

        "WiFi": [
            "Check if Wi-Fi is enabled.",
            "Restart the router.",
            "Reconnect to the Wi-Fi network.",
            "Verify internet connectivity."
        ]
    }

    return {
        "category": category,
        "troubleshooting_steps": troubleshooting_db.get(
            category,
            ["No troubleshooting steps found."]
        )
    }


# Optional alias for compatibility with older code
def troubleshoot_issue(category):
    return get_troubleshooting_steps(category)