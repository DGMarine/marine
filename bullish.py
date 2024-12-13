import requests
import json

# Google Sheet Details
SHEET_ID = "1BZD3KMudab4yz-3yfIT_oMC8e3TcY17_kNXOXjdiQ1o"
API_KEY = "AIzaSyAu198-qYfAlguW3F0rZSHGtb6lns6xSm"
SHEET_NAME = "bullish"
RANGE = "A8:Z250"

# URL to fetch data
url = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{SHEET_NAME}!{RANGE}?key={API_KEY}"

# Fetch data from Google Sheets API
response = requests.get(url)
data = response.json()

# Extract rows and create a list of dictionaries
columns = ["name", "symbol", "prices", "open", "low", "br", "t2", "t1", "s1", "s2", "sr", "high", "point"]
rows = data.get("values", [])
json_data = [dict(zip(columns, row)) for row in rows[1:]]  # Skip the header row if present

# Save JSON file
json_file_path = "bullish_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"Data saved to {json_file_path}")
