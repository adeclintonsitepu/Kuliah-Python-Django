# Development Framework Django

Proyek-proyek sederhana Framework Django

### Requirements
<ul>
<li>Virtual Environtment</li>
<li>Python versi 3.10.*</li>
<li>Django versi 4.2.*</li>
<li>pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib </li>
</ul>

<hr>

### Cloning the repository

Clone the repository using the command below :
```bash
git clone https://github.com/adeclintonsitepu/Kuliah-Python-Django.git

```

Move into the directory where we have the project files : 
```bash
cd websiteku

```

Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

Activate the virtual environment :
```bash
envname\scripts\activate

```

<hr>

### Running the App

To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

<h1>Connect Django to Google Spreadsheet</h1>

<p>To access and manipulate cells in a Google Spreadsheet from a Django application, you can use the Google Sheets API. Here are the steps to integrate Google Sheets API with Django:</p>

<h3>Step 1: Set Up Google Sheets API</h3>
<ol>
  <li>Enable Google Sheets API:</li>
  <ul>
    <li>Go to the Google Cloud Console.</li>
    <li>Create a new project or select an existing one.</li>
    <li>Navigate to the "API & Services" > "Library" and enable the "Google Sheets API".</li>
    <li>Also, enable the "Google Drive API" to manage spreadsheet files.</li>
  </ul>
  <li>Create Credentials:</li>
  <ul>
    <li>Go to "API & Services" > "Credentials".</li>
    <li>Click "Create Credentials" and select "Service Account".</li>
    <li>Fill in the required details and create the service account.</li>
    <li>Once created, go to the "Keys" section and add a key. Choose JSON format to download the credentials file.</li>
  </ul>
  <li>Share the Spreadsheet with the Service Account:</li>
  <ul>
    <li>Open your Google Spreadsheet.</li>
    <li>Share the spreadsheet with the email address of the service account (found in the JSON file).</li>
  </ul>  
</ol>
<h3>Step 2: Install Required Libraries</h3>
Install the Google API client library using pip:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

<h3>Step 3: Configure Django to Use the API</h3>
<ol>
  <li>Add the JSON Credentials File to Your Django Project:</li>
  <ul>
    <li>Place the downloaded JSON credentials file in your Django project directory (e.g., settings/credentials.json).</li>
  </ul>
  <li>Update Your Django Settings:</li>
  Add the path to your credentials file in your 'settings.py'.

```bash
import os

BASE_DIR_1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOOGLE_SHEETS_CREDENTIALS = os.path.join(BASE_DIR_1, 'settings', 'credentials.json')
```
  <li>Create a Utility Function to Access Google Sheets:</li>
  Create a new file, e.g., utils/google_sheets.py, and add the following code:

```bash
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

def get_sheet_values(spreadsheet_id, range_name):
    service = get_google_sheets_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return values

def update_sheet_values(spreadsheet_id, range_name, values):
    service = get_google_sheets_service()
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='RAW', body=body).execute()
    return result
```
</ol>

<h3>Step 4: Use the Utility Functions in Your Django Views</h3>
<ol>
  <li>Create a View to Read and Update Google Sheets:</li>
  views.py

  ```bash
from django.shortcuts import render
from .utils.google_sheets import get_sheet_values, update_sheet_values

def read_sheet(request):
    spreadsheet_id = 'your_spreadsheet_id'
    values = get_sheet_values(spreadsheet_id)
    return render(request, 'read_sheet.html', {'values': values})
```
  <li>Create Templates:</li>
  Create read_sheet.html in your templates directory to display the results.

```bash
<!DOCTYPE html>
<html>
<head>
    <title>Read Google Sheets</title>
</head>
<body>
    <h1>Google Sheets Data</h1>
    <table border="1">
        {% for row in values %}
        <tr>
            {% for cell in row %}
            <td>{{ cell }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```
<li>Configure URLs:</li>
Add the views to your urls.py:

```bash
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('read-sheet/', views.read_sheet, name='read_sheet'),
]
```

</ol>

