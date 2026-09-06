# Master dictionary used to store all support tickets.
tickets = {}

# Counter used to generate unique ticket IDs.
ticket_counter = 1000

# ==============================
# Main menu display function
# ==============================

def display_menu():
    print("\n=================================")
    print("     IT SUPPORT TICKET SYSTEM")
    print("=================================")
    print("1. Create Ticket")
    print("2. View All Tickets")
    print("3. Search Ticket")
    print("4. Update Ticket")
    print("5. Close Ticket")
    print("6. View Ticket Statistics")
    print("7. Exit")

# ==============================
# Menu option 1 function
# ==============================

def create_ticket():
    # Allows the function to update the global ticket counter.
    global ticket_counter

    # Increase the counter and generate a unique ticket ID.
    ticket_counter += 1
    ticket_id = f"INC{ticket_counter}"

    print("\n--- Create New Ticket ---")

    # Collect ticket information from the user.
    user = input("Enter user name: ")
    department = input("Enter department: ")
    category = input("Enter issue category: ")
    description = input("Describe the issue: ")
    
    # Collect and validate the ticket priority.
    while True:
        priority = input("Enter priority (Low/Medium/High): ").title()

        if priority in ["Low", "Medium", "High"]:
            break

        print("Invalid priority. Please enter Low, Medium, or High.")


    # Store the new ticket in the master dictionary.
    tickets[ticket_id] = {
        "user": user,
        "department": department,
        "category": category,
        "description": description,
        "priority": priority,
        "status": "Open",
        "technician": "Unassigned"
    }

    print(f"\nTicket created successfully with ID: {ticket_id}")

# ==============================
# Menu option 2 function
# ==============================

def view_tickets():
    # Check whether any tickets have been created.
    if not tickets:
        print("\nNo tickets found.")
        return

    print("\n--- All Support Tickets ---")

    # Loop through each ticket and display its information.
    for ticket_id, ticket in tickets.items():
        print(f"\nTicket ID: {ticket_id}")
        print(f"User: {ticket['user']}")
        print(f"Department: {ticket['department']}")
        print(f"Category: {ticket['category']}")
        print(f"Description: {ticket['description']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print(f"Technician: {ticket['technician']}")
        print("-" * 35)

# ==============================
# Menu option 3 function
# ==============================

def search_ticket():
    # Ask the user for the Ticket ID they want to find.
    ticket_id = input("\nEnter Ticket ID to search: ").upper()

    # Check whether the Ticket ID exists in the tickets dictionary.
    if ticket_id in tickets:
        ticket = tickets[ticket_id]

        print("\n--- Ticket Found ---")
        print(f"\nTicket ID: {ticket_id}")
        print(f"User: {ticket['user']}")
        print(f"Department: {ticket['department']}")
        print(f"Category: {ticket['category']}")
        print(f"Description: {ticket['description']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print(f"Technician: {ticket['technician']}")
        print("-" * 35)

    else:
        print("\nTicket not found.")

# ==============================
# Menu option 4 function
# =============================
        
def update_ticket():
    # Ask the user for the Ticket ID they want to update.
    ticket_id = input("\nEnter Ticket ID to update: ").upper()

    # Check whether the Ticket ID exists.
    if ticket_id in tickets:
        ticket = tickets[ticket_id]

        print("\n--- Update Ticket ---")
        print("1. Update Priority")
        print("2. Update Status")
        print("3. Assign Technician")

        choice = input("\nSelect an option (1-3): ")

        if choice == "1":
            # Collect and validate the new ticket priority.
            while True:
                priority = input(
                    "Enter new priority (Low/Medium/High): "
                ).title()

                if priority in ["Low", "Medium", "High"]:
                    ticket["priority"] = priority
                    break

                print("Invalid priority. Please enter Low, Medium, or High.")

        elif choice == "2":
            # Collect and validate the new ticket status.
            while True:
                status = input(
                    "Enter new status (Open/In Progress/Closed): "
                ).title()

                if status in ["Open", "In Progress", "Closed"]:
                    ticket["status"] = status
                    break

                print("Invalid status. Please enter Open, In Progress, or Closed.")

        elif choice == "3":
            ticket["technician"] = input(
                "Enter technician name: "
            )

        else:
            print("\nInvalid selection.")
            return

        print(f"\nTicket {ticket_id} updated successfully!")

    else:
        print("\nTicket not found.")



# ==============================
# Menu option 5 function
# ==============================

def close_ticket():
    # Ask the user for the Ticket ID they want to close.
    ticket_id = input("\nEnter Ticket ID to close: ").upper()

    # Check whether the Ticket ID exists.
    if ticket_id in tickets:
        # Update the ticket status to Closed.
        tickets[ticket_id]["status"] = "Closed"

        print(f"\nTicket {ticket_id} has been closed successfully.")

    else:
        print("\nTicket not found.")



# ==============================
# Menu option 6 function
# ==============================

def ticket_statistics():
    # Count the total number of tickets.
    total_tickets = len(tickets)

    # Create counters for each ticket status.
    open_tickets = 0
    in_progress_tickets = 0
    closed_tickets = 0

    # Loop through all tickets and count each status.
    for ticket in tickets.values():
        if ticket["status"] == "Open":
            open_tickets += 1

        elif ticket["status"] == "In Progress":
            in_progress_tickets += 1

        elif ticket["status"] == "Closed":
            closed_tickets += 1

    # Display the ticket statistics.
    print("\n--- Ticket Statistics ---")
    print(f"Total Tickets: {total_tickets}")
    print(f"Open Tickets: {open_tickets}")
    print(f"In Progress Tickets: {in_progress_tickets}")
    print(f"Closed Tickets: {closed_tickets}")


# ==============================
# Main section of the program that runs the menu loop
# ==============================
def main():
    while True:
        display_menu()
        choice = input("\nSelect an option (1-7): ")

        if choice == "1":
            create_ticket()

        elif choice == "2":
            view_tickets()

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            update_ticket()

        elif choice == "5":
            close_ticket()

        elif choice == "6":
            ticket_statistics()

        elif choice == "7":
            print("\nThank you for using the IT Support Ticket System.")
            break

        else:
            print("\nInvalid selection. Please choose an option from 1-7.")


if __name__ == "__main__":
    main()

