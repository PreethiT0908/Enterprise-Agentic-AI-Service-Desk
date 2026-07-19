from agents.automation_agent import automate_resolution


def test_automation():

    test_cases = [
        "VPN",
        "Printer",
        "Password",
        "Email",
        "WiFi",
        "Software",
        "Unknown"
    ]


    for category in test_cases:

        result = automate_resolution(category)

        print("\nCATEGORY:", category)
        print("AUTOMATION RESULT:")
        print(result)


if __name__ == "__main__":
    test_automation()