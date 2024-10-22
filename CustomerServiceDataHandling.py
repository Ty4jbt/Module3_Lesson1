# Task 1

# Initial dictionary of service tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Adds a new ticket to the dictionary with the given ticket ID, customer name, and issue into the selected dictionary
def open_ticket(ticket_id, customer_name, issue, ticket_dict):
    ticket_dict[ticket_id] = {"Customer": customer_name, "Issue": issue, "Status": "open"}
    return ticket_dict

# Updates the status of a ticket by finding the ticket ID in the selected dictionary and changing the status to the new status
def update_ticket_status(ticket_id, new_status, ticket_dict):
    if ticket_id in ticket_dict:
        ticket_dict[ticket_id]["Status"] = new_status
    return ticket_dict

# Displays all tickets in the selected dictionary, with an optional status filter to only show tickets with a specific status
def display_tickets(ticket_dict, status_filter=None):
    if status_filter:
        filtered_tickets = {ticket_id: details for ticket_id, details in ticket_dict.items() if details["Status"] == status_filter}
        return filtered_tickets
    return ticket_dict

# Open a new ticket
service_tickets = open_ticket("Ticket003", "Charlie", "Technical issue", service_tickets)

# Update the status of an existing ticket
service_tickets = update_ticket_status("Ticket001", "closed", service_tickets)

# Display all tickets
all_tickets = display_tickets(service_tickets)
print("All Tickets:")
for ticket_id, details in all_tickets.items():
    print(f"{ticket_id}: {details}")

# Display only closed tickets
closed_tickets = display_tickets(service_tickets, "closed")
print("\nClosed Tickets:")
for ticket_id, details in closed_tickets.items():
    print(f"{ticket_id}: {details}")