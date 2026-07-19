def make_decision(automation_result):

    if automation_result["status"] == "SUCCESS":

        return {
            "resolved": True,
            "next_action": "Close Incident"
        }


    return {
        "resolved": False,
        "next_action": "Create Ticket"
    }