from agents.decision_agent import make_decision


def test_decision():

    test_cases = [

        {
            "action": "Restart Print Spooler",
            "status": "SUCCESS"
        },

        {
            "action": "Restart VPN Client",
            "status": "FAILED"
        }

    ]


    for automation in test_cases:

        result = make_decision(automation)

        print("\nAUTOMATION:")
        print(automation)

        print("DECISION:")
        print(result)


if __name__ == "__main__":
    test_decision()