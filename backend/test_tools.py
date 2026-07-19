from tools.system_tools import (
    restart_print_spooler,
    restart_network_adapter,
    restart_vpn
)


print("\nPRINT SPOOLER")
print(restart_print_spooler())


print("\nNETWORK")
print(restart_network_adapter())


print("\nVPN")
print(restart_vpn())