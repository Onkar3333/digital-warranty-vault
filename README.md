# Digital Warranty Vault

A MicroSaaS solution to manage and track product warranties with automated expiry notifications.

## Features
- Add product details, purchase dates, and warranty periods.
- Receive reminders before warranties expire.
- View all warranties in one place.
- Simple API to integrate with other tools.

## Installation
1. Clone this repository:

   git clone https://github.com/Onkar3333/digital-warranty-vault.git
   
2. Navigate to the project folder:
cd digital-warranty-vault

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
python app.py

5. Dependencies
Flask
Flask-SQLAlchemy
SQLite
Python (>=3.8)

6. Usage
Start the server:
Visit http://127.0.0.1:5000 to interact with the API.
API Endpoints:
GET /api/warranties: Fetch all warranties.
POST /api/warranties: Add a new warranty.
DELETE /api/warranties/<id>: Delete a warranty by ID.

7. Future Improvements
Add OCR functionality for receipt uploads.
Implement a user-friendly frontend dashboard.
Enable multi-user support.
