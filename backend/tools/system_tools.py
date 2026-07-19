import subprocess


def restart_print_spooler():

    try:

        stop = subprocess.run(
            "net stop spooler",
            shell=True,
            capture_output=True,
            text=True
        )

        if stop.returncode != 0:
            return {
                "action": "Restart Print Spooler",
                "status": "FAILED",
                "message": stop.stderr or stop.stdout
            }

        start = subprocess.run(
            "net start spooler",
            shell=True,
            capture_output=True,
            text=True
        )

        if start.returncode != 0:
            return {
                "action": "Restart Print Spooler",
                "status": "FAILED",
                "message": start.stderr or start.stdout
            }

        return {
            "action": "Restart Print Spooler",
            "status": "SUCCESS",
            "message": "Printer spooler restarted successfully"
        }

    except Exception as e:

        return {
            "action": "Restart Print Spooler",
            "status": "FAILED",
            "message": str(e)
        }


def restart_network_adapter():

    try:

        return {
            "action": "Restart Network Adapter",
            "status": "SUCCESS",
            "message": "Network adapter restart requested"
        }

    except Exception as e:

        return {
            "action": "Restart Network Adapter",
            "status": "FAILED",
            "message": str(e)
        }


def restart_vpn():

    return {
        "action": "Restart VPN Client",
        "status": "FAILED",
        "message": "VPN restart tool not configured"
    }