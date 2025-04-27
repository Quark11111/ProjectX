import gspread
import os
import json
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

creds_json = os.getenv('GOOGLE_CREDS_JSON')
if creds_json is None:
    raise ValueError("Переменная окружения GOOGLE_CREDS_JSON не установлена!")

creds_dict = json.loads(creds_json)

CREDS = Credentials.from_service_account_file(creds_dict, scopes=SCOPES)

def save_to_google_sheet(name: str, phone: str):
    try:
        gc = gspread.authorize(CREDS)
        sh = gc.open('Quarks Applications')
        sheet = sh.sheet1
        sheet.append_row([datetime.now().strftime('%Y-%m-%d %H:%M'), name, phone])
        print("Данные успешно сохранены в Google Sheets.")
    except gspread.exceptions.APIError as e:
        print(f"Ошибка API: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    
