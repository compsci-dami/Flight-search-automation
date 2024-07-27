# Flight-deals-automation

This project is a Python automation program that allows users to sign up, provide their name and email, and get added to a spreadsheet using the Google Sheets API. The project integrates the Google Sheets API, and the smtplib module to create a flight deals subscription system.

<h2>Features</h2
              
User Signup: Users can sign up, providing their name and email.
Spreadsheet Integration: User information is added to a Google Sheet for easy management.
Flight Deals Search: The program searches for flight deals that match destinations and price criteria specified in the Google Sheet.
Notification System: When a matching deal is found, users are notified via telephone message using the Twilio API.
Flight Search API: The flight search functionality is powered by the Amadeus API, though the Tequila API by Kiwi.com can also be used.

<h2>Technologies Used</h2>

Google Sheets API: For storing and managing user data.
smtplib: For sending emails.
Twilio API: For sending telephone notifications to users.
Amadeus API: For searching flight deals. (Tequila API by Kiwi.com can also be used as an alternative.)
Getting Started
Prerequisites
Python 3.x
Google API credentials (Google Sheets)
Twilio account and credentials
Amadeus API credentials (or Tequila API credentials)
