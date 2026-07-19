from agents.incident_agent import analyze_incident

user_issue = "My VPN is not connecting after password reset"

incident_result = analyze_incident(user_issue)

print(incident_result)