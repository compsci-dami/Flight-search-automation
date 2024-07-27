print("Welcome to Fight Club.")
print("We find the best flight deals and email you.")

user_first_name = input("What is your first name?\n")
user_last_name = input("What is your last name?\n")
user_email = input("What is your email?\n")
user_email_verified = input("What is your email?\n")

if user_email == user_email_verified:
  print("You are in the club!")

#___________________________________________________#
""""ADD this information to google sheet through api"""
import requests

url = "https://api.sheety.co/b6f4a2f544566d0543eba035b9507218/flightDeals/users"

payload = {
    "user": {
        "firstName": user_first_name,
        "lastName": user_last_name,
        "email": user_email
    }
}
# Make the POST request
response = requests.post(url, json=payload)
# Check if the request was successful
if response.status_code in (200, 201):
  print("User data successfully posted.")
else:
  print("Failed to post data. Status code:", response.status_code)
  print("Response:", response.text)
