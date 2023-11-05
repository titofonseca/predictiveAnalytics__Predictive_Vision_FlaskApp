"""
Google Analytics Data Forecasting Script
----------------------------------------

Streamlines the process of fetching, forecasting, and exporting Google Analytics data.

Description:
    This script coordinates multiple stages:

    1. Retrieval of data from both Universal Analytics and Google Analytics 4 (GA4).
    2. Data merging for a comprehensive dataset.
    3. Time series forecasting utilizing Facebook's Prophet.
    4. Exportation of the forecasted data to Google Sheets.

Dependencies:
    - Google Analytics Data API v1beta and Reporting API v4: Data retrieval from GA4 and UA, respectively.
    - Facebook's Prophet: Time series forecasting.
    - gspread: Google Sheets interactions.
    - dotenv: Environment variable management from the .env file.

Main Functions:
    - main(): Coordinates the entire data fetching, forecasting, and exportation workflow.

Usage:
    Intended to be run as the primary script to automate the forecasting process. 
    Ensure all necessary modules and dependencies are in place before execution.
"""

import os
import pandas as pd
from dotenv import load_dotenv
from modules.ga4 import fetch_ga4_data
from modules.ua import fetch_ua_data  # Assuming the UA fetching function is named fetch_ua_data in ua.py
from modules.prophet_model import run_prophet_forecasting
from modules.gsheet_export import export_to_gsheet
import logging
logging.getLogger('cmdstanpy').setLevel(logging.WARNING)

def main():
    load_dotenv()
    print("Loaded GOOGLE_SERVICE_KEY_PATH:", os.environ.get('GOOGLE_SERVICE_KEY_PATH'))

    try:
        df_ga4 = fetch_ga4_data()
    except Exception as e:
        print(f"Error fetching data from GA4: {e}")
        return
    
    try:
        df_ua = fetch_ua_data()
    except Exception as e:
        print(f"Error fetching data from UA: {e}")
        return
    
    # Convert 'ds' columns to datetime type
    df_ga4['ds'] = pd.to_datetime(df_ga4['ds'])
    df_ua['ds'] = pd.to_datetime(df_ua['ds'])
    
    # Combining GA4 and UA data
    df_combined = pd.concat([df_ua, df_ga4], ignore_index=True)
    
    try:
        forecast_df = run_prophet_forecasting(df_combined)
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