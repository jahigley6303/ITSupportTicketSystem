 =================================
 ###    IT SUPPORT TICKET SYSTEM
 =================================



A command-line IT support ticket management application built with Python. The application allows users to create, view, search, update, and close support tickets while tracking ticket statistics.

## Features

- Create new IT support tickets with automatically generated ticket IDs
- View all support tickets
- Search for tickets by Ticket ID
- Update ticket priority, status, and assigned technician
- Close support tickets while preserving ticket history
- View ticket statistics by status
- Input validation for priorities and ticket statuses
- Error handling for invalid ticket IDs and menu selections

## Technologies Used

- Python
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Input Validation
- Error Handling

## How It Works

The application provides a menu-driven interface with the following options:

1. Create Ticket
2. View All Tickets
3. Search Ticket
4. Update Ticket
5. Close Ticket
6. View Ticket Statistics
7. Exit

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/jhigley6303/ITSupportTicketSystem.git
```

2. Navigate to the project directory:
```bash
cd IT-Support-Ticket-System
```
4. Run the application:
python main.py

### Ticket Information

Each support ticket includes:

- Ticket ID
- User
- Department
- Issue Category
- Description
- Priority
- Status
- Assigned Technician

### Input Validation

The application validates user input for:
- Priority: Low, Medium, or High
- Status: Open, In Progress, or Closed
- Valid ticket IDs when searching, updating, or closing tickets
- Valid menu selections

### Future Improvements

Potential future improvements include:
- Persistent ticket storage using JSON
- Database integration
- User authentication
- Additional ticket categories
- Advanced reporting and analytics
- Graphical user interface (GUI)
- Web-based version

### Author

Jamie Pascual

IT / Systems & Support Portfolio
