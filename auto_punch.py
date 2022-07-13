import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import dotenv_values, load_dotenv
import time
load_dotenv()

SHEET_KEY = dotenv_values()["SHEET_KEY"]

def google_sheet():
    scopes = ["https://spreadsheets.google.com/feeds"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scopes
    )
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_KEY).sheet1
    sheet.update_cell(2, 2, "9:00")
    sheet.update_cell(2, 3, "18:30")
    sheet.update_cell(2, 4, "8")


google_sheet()
