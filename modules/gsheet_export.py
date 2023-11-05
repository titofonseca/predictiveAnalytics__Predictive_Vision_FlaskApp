"""
Google Sheets Data Export Module
-------------------------------
Handles the process of exporting DataFrame content to Google Sheets, leveraging the gspread library for authentication and interactions with Google's Sheets API.

Description:
    This module is specifically designed to facilitate the export of forecasted data, particularly from the Prophet model, to Google Sheets. The functionality ensures that data is seamlessly updated in an existing sheet or, if necessary, a new sheet is created to accommodate the data.

Dependencies:
    - gspread: Interface for Google Sheets operations.
    - oauth2client: Authentication using service accounts.
    - gspread_dataframe: Utility for transferring pandas DataFrame data to Google Sheets.
    - json: JSON data processing.

Main Functions:
    - export_to_gsheet(df_f, sheet_name="Prophet"): Manages the export of a DataFrame to a designated Google Sheet, handling authentication, sheet interactions, and data transfers.
"""

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
import json

# Configurations
Key = os.environ.get('GOOGLE_SERVICE_KEY_PATH')
Google_Sheets_ID = os.environ.get('GOOGLE_SHEETS_ID')

def export_to_gsheet(df_f, sheet_name="Prophet"):
    """Export DataFrame to a specified Google Sheet."""
    try:
        gc = gspread.service_account(filename=Key)
        spreadsheet = gc.open_by_key(Google_Sheets_ID)
        
        try:
            worksheet = spreadsheet.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows="1000", cols="20")
        
        # Reorder the columns before exporting
        df_f = df_f[['Date', 'Real Sales', 'Predicted Sales', 'Lower Bound', 'Upper Bound']]
        
        worksheet.clear()
        set_with_dataframe(worksheet, df_f, include_index=False, include_column_header=True, resize=True)
        print(f"Data exported to {sheet_name} successfully!")

    except gspread.exceptions.APIError as e:
        print(f"API Error: {e}")
    except gspread.exceptions.GSpreadException as e:
        print(f"gspread Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()