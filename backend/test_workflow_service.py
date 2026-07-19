from service.workflow_service import process_incident

result = process_incident(
    "My VPN is not connecting after password reset"
)

print(result)