from tools.system_tools import (
    restart_print_spooler,
    restart_network_adapter,
    restart_vpn
)


def automate_resolution(category):

    if category == "Printer":
        return restart_print_spooler()

    elif category == "WiFi":
        return restart_network_adapter()

    elif category == "VPN":
        return restart_vpn()

    elif category == "Password":
        return {
            "action": "Unlock User Account",
            "status": "SUCCESS"
        }

    elif category == "Email":
        return {
            "action": "Restart Outlook Service",
            "status": "SUCCESS"
        }

    else:
        return {
            "action": "No Automation Available",
            "status": "FAILED"
        }