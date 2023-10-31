"""
Google Sheets Export Module

Description:
This module facilitates the process of exporting data to Google Sheets. It uses the gspread library to authenticate and interact with the Google Sheets API. The forecasted data from the Prophet model is exported to a specified Google Sheet, either updating an existing sheet or creating a new one if it doesn't exist.

Dependencies:
- gspread: The main library used to interact with Google Sheets.
- oauth2client: Used for service account authentication.
- gspread_dataframe: Helper library to export pandas DataFrames to Google Sheets.
- json: For handling JSON data.

Main Functions:
- export_to_gsheet(df_f, sheet_name="Prophet"): Exports a DataFrame to a specified Google Sheet. The sheet name defaults to "Prophet" but can be overridden. The function handles authentication, sheet creation or updating, and DataFrame export.
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