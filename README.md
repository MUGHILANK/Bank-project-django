# SIB Banking System

This is a simple banking system built using Django. The project allows users to register, create bank accounts, deposit and withdraw money, and check their account balance. It also sends a confirmation email when a user creates a new account.

## Features

- **User Registration**: Users can register with their name, email, and password.
- **Account Creation**: Users can create a new bank account with a unique account number, mobile number, and password.
- **Login**: Users can log in to their account using their email and password.
- **Account Verification**: Users can verify their account details such as account number, mobile number, and password.
- **Deposit**: Users can deposit money into their account.
- **Withdraw**: Users can withdraw money from their account.
- **Transaction History**: Users can view a history of their transactions (deposits and withdrawals).
- **Email Notifications**: The system sends an email to users with their account number after registration.

## Installation

To set up the project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sib-banking-system.git
cd sib-banking-system

2. Set Up Virtual Environment
It is recommended to create a virtual environment to manage dependencies.
  python3 -m venv venv
  source venv/bin/activate  # For Linux/MacOS
  venv\Scripts\activate     # For Windows

3. Install Dependencies
pip install -r requirements.txt

4. Set Up the Database
Run migrations to set up the database:
  python manage.py migrate

5. Run the Development Server
Start the development server:
  python manage.py runserver

Project Structure:

sib_banking_system/
├── manage.py              # Django management script
├── sib_banking/           # Main app for the banking system
│   ├── migrations/        # Database migrations
│   ├── __init__.py
│   ├── admin.py           # Django admin configurations
│   ├── apps.py            # App configurations
│   ├── models.py          # Models for database tables
│   ├── tests.py           # Unit tests
│   └── views.py           # Views for handling requests
├── templates/             # HTML templates for rendering views
│   ├── account_verification.html
│   ├── create_new_acc.html
│   ├── deposit.html
│   ├── home.html
│   ├── Transaction_History.html
│   ├── bank_balance.html
│   └── SIB_login.html
├── requirements.txt       # Python dependencies
└── settings.py            # Django project settings


License
This project is open-source and available under the MIT License.

csharp
Copy code

You can replace the project URL and adjust the sections as per your preferences.

Screenshot
