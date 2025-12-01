import requests
from discord.ext import commands
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

class SheetsService:
    def __init__(self):
        load_dotenv()
        self.serviceID = os.getenv('SERVICE_ID')
        self.servicePassword = os.getenv('SERVICE_PASSWORD')
        self.spreadsheetID = os.getenv('BD_CONNECTION_SPREADSHEET')
        self.range=os.getenv('CONNECTION_BD_RANGE')

    def AtualizarBD(self, data_payload):
        url = (
            f"https://sheets.googleapis.com/v4/spreadsheets/{self.spreadsheetID}/values/"
            f"{self.range}:append?valueInputOption=USER_ENTERED"
        )
        headers = {
            'Authorization': f'Bearer {self.serviceToken}', # É essencial usar um token Bearer
            'Content-Type': 'application/json'
        }
        payload = {
            "values": data_payload # data_payload deve ser um array de arrays
        }
        try:
            response = requests.post(url, headers=headers, json=payload)

            # 6. Tratar a resposta
            if response.status_code == 200:
                print("✅ Dados anexados com sucesso!")
                return response.json()
            else:
                print(f"❌ Erro ao anexar dados. Status: {response.status_code}")
                print(f"Resposta da API: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão HTTP: {e}")
            return None