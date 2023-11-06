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
from modules.ua import fetch_ua_data
from modules.prophet_model import run_prophet_forecasting
import logging

logging.getLogger('cmdstanpy').setLevel(logging.WARNING)

# Metric mapping for display name retrieval
METRIC_MAP_GA4 = {
    'Revenue': 'totalRevenue',
    'Sessions': 'sessions',
    'Conversions': 'ecommercePurchases'
}

METRIC_MAP_UA = {
    'Revenue': 'ga:transactionRevenue',
    'Sessions': 'ga:sessions',
    'Conversions': 'ga:transactions'
}

def get_display_name_for_metric(metric):
    for display_name, tech_name in METRIC_MAP_GA4.items():
        if tech_name == metric:
            return display_name
    for display_name, tech_name in METRIC_MAP_UA.items():
        if tech_name == metric:
            return display_name
    return "Metric"

def main(metric_ga4='totalRevenue', metric_ua='ga:transactionRevenue'):
    load_dotenv()

    # Retrieve display name for metrics
    metric_display_name_ga4 = get_display_name_for_metric(metric_ga4)
    metric_display_name_ua = get_display_name_for_metric(metric_ua)
    
    try:
        df_ga4 = fetch_ga4_data(metric_ga4)
    except Exception as e:
        print(f"Error fetching data from GA4: {e}")
        return
    
    try:
        df_ua = fetch_ua_data(metric_ua)
    except Exception as e:
        print(f"Error fetching data from UA: {e}")
        return
    
    # Convert 'ds' columns to datetime type
    df_ga4['ds'] = pd.to_datetime(df_ga4['ds'])
    df_ua['ds'] = pd.to_datetime(df_ua['ds'])
    
    # Combining GA4 and UA data
    df_combined = pd.concat([df_ua, df_ga4], ignore_index=True)
    
    try:
        forecast_df = run_prophet_forecasting(df_combined, metric_name=metric_display_name_ga4)
    except Exception as e:
        print(f"Error running Prophet forecasting: {e}")
        return

    return forecast_df

if __name__ == "__main__":
    main()