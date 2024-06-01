from django.shortcuts import render
from .google_sheets import get_sheet_values, get_spreadsheet_name

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def tabel(request):
    spreadsheet_id = '1dbAZ2PIWXDs1-KAI6Czq2-YMFPhggep2nnDSb2rfYUQ'
    values1, values2 = get_sheet_values(spreadsheet_id)
    sheet_name = get_spreadsheet_name(spreadsheet_id)
    context = {'values1': values1, 'values2': values2, 'sheet_name': sheet_name}
    return render(request, 'base/tabel.html', context)

def read_sheet(request):
    spreadsheet_id = '1dbAZ2PIWXDs1-KAI6Czq2-YMFPhggep2nnDSb2rfYUQ'
    sheet_name = get_spreadsheet_name(spreadsheet_id)
    context = {'values': values, 'sheet_name': sheet_name}
    return render(request, 'base/read_sheet.html', context)
