"""
Time Series Forecasting Script for Google Analytics 4 Data

Description:
This script orchestrates the process of fetching data from Google Analytics 4 (GA4), running a time series forecast using Facebook's Prophet, and exporting the forecast to Google Sheets. The data fetched from GA4 represents the total revenue over a specified period, which is then used to forecast future revenues.

Dependencies:
- Google Analytics Data API v1beta: For fetching data from GA4.
- Facebook's Prophet: For time series forecasting.
- gspread: For exporting data to Google Sheets.
- dotenv: For loading environment variables from the .env file.

Main Functions:
- main() : The primary function that organizes the entire forecasting process. It manages the steps of data fetching from GA4, forecasting using Prophet, and exporting the forecasted results to Google Sheets.
"""

import os
from dotenv import load_dotenv
from modules.ga4 import fetch_ga4_data
from modules.prophet_model import run_prophet_forecasting
from modules.gsheet_export import export_to_gsheet

def main():
    load_dotenv()
    print("Loaded GOOGLE_SERVICE_KEY_PATH:", os.environ.get('GOOGLE_SERVICE_KEY_PATH'))

    try:
        df = fetch_ga4_data()
    except Exception as e:
        print(f"Error fetching data from GA4: {e}")
        return
    
    try:
        forecast_df = run_prophet_forecasting(df)
    except Exception as e:
        print(f"Error running Prophet forecasting: {e}")
        return

    try:
        export_to_gsheet(forecast_df)
        print("Forecast exported to Google Sheets successfully.")
    except Exception as e:
        print(f"Error exporting forecast to Google Sheets: {e}")

if __name__ == "__main__":
    main()