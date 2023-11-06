"""
GA4 Data Fetching Module
-------------------------
Fetches revenue data from Google Analytics 4 (GA4) using the Google Analytics Data API v1beta and structures it into a pandas DataFrame.

Description:
    This module facilitates the data retrieval process from GA4, processes the API response, and organizes the data for further analysis. 
    The primary aim is to obtain the total revenue for a specified period in a structured format.

Dependencies:
    - google.analytics.data_v1beta: Interface to GA4 Data API.
    - pandas: Data manipulation and analysis.
    - dotenv: Environment variable management from .env file.
    - json: JSON data handling.

Main Functions:
    - initialize_analyticsreporting(): Sets up the GA4 Data API v1beta client.
    - get_report(client): Fetches GA4 data based on predefined configurations.
    - fetch_ga4_data(): Master function to manage the data retrieval process.
"""

import os
import pandas as pd
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Configurations
Key = os.environ.get('GOOGLE_SERVICE_KEY_PATH')
Property = os.environ.get('GA4_PROPERTY_ID')

def initialize_analyticsreporting():
    with open(Key, 'r') as file:
        service_account_info = json.load(file)
    client = BetaAnalyticsDataClient.from_service_account_info(service_account_info)
    return client

def get_report(client, metric="totalRevenue"):
    start_date = datetime(2023, 8, 1)
    days_ago = (datetime.now() - start_date).days
    request = RunReportRequest(
        property=f"properties/{Property}",
        date_ranges=[DateRange(start_date=f"{days_ago}daysAgo", end_date="yesterday")],
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name=metric)],
        keep_empty_rows=True
    )
    return client.run_report(request)


def fetch_ga4_data(metric="totalRevenue"):
    try:
        client = initialize_analyticsreporting()
        response = get_report(client, metric)
        finalRows = []
        for row in response.rows:
            date = row.dimension_values[0].value
            value = float(row.metric_values[0].value)
            finalRows.append({'ds': date, 'y': value})
        return pd.DataFrame(finalRows)
    except Exception as e:
        print(f"Error fetching data from GA4: {e}")
        return None
