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
 
    # find empty cell and update it
    for i in range(1, 1000):
        if sheet.cell(i, 2).value == None:
            sheet.update_cell(i, 2, "9:00")
            sheet.update_cell(i, 3, "18:30")
            sheet.update_cell(i, 4, "8")
            break
    print("punched!")


google_sheet()
