import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings

def get_google_sheets_service():
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_SHEETS_CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    )
    service = build('sheets', 'v4', credentials=credentials)
    return service

def get_google_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_SHEETS_CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/drive']
    )
    service = build('drive', 'v3', credentials=credentials)
    return service

def get_sheet_values(spreadsheet_id):
    service = get_google_sheets_service()
    sheet = service.spreadsheets()
    daftar_nilai = sheet.values().get(spreadsheetId=spreadsheet_id, range='Sheet1').execute()
    daftar_password = sheet.values().get(spreadsheetId=spreadsheet_id, range='Sheet2').execute()
    values1 = daftar_nilai.get('values', [])
    values2 = daftar_password.get('values', [])
    return values1, values2

def get_spreadsheet_name(spreadsheet_id):
    drive_service = get_google_drive_service()
    file = drive_service.files().get(fileId=spreadsheet_id, fields='name').execute()
    return file.get('name')
